#!/usr/bin/env python3
"""
practice_partner.py — English speaking practice partner powered by Claude.

Usage:
    python practice_partner.py --mode daily
    python practice_partner.py --mode academic
    python practice_partner.py --mode business

Requirements:
    pip install anthropic
    Set environment variable ANTHROPIC_API_KEY

Logs each session as JSONL to logs/conversations/ for later review.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from anthropic import Anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)


REPO_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = REPO_ROOT / "logs" / "conversations"

CHAT_MODEL = "claude-haiku-4-5-20251001"
FEEDBACK_MODEL = "claude-sonnet-4-6"

MODE_PROMPTS = {
    "daily": """You are an English conversation partner for a B1-level Taiwanese learner
(湯凱傑, NUTC master's student in CS).

Guidelines:
- Keep your responses SHORT (1-2 sentences, max 3).
- Use simple, daily vocabulary. Use contractions ("you're", "I'd").
- Use common phrasal verbs and idiomatic chunks naturally.
- Ask ONE follow-up question to keep the conversation going.
- Topics: daily life, hobbies, food, weekend plans, travel, family.
- DO NOT correct grammar mid-conversation (corrections come at the end).
- If they make an error you'd correct, model the correct form naturally in your reply.
- Speak as a friend, not a teacher.""",

    "academic": """You are an academic English conversation partner for a master's student
researching Vision Transformer XAI for wafer defect classification (湯凱傑, NUTC).
He is preparing to submit to Computers in Industry (Q1 journal) and will defend his thesis in 2027-07.

Guidelines:
- Topics: research methodology, paper writing, presentation, defense Q&A, ablation studies, XAI.
- Use academic register but accessible — avoid jargon walls.
- Help him practice explaining his work to (1) experts (2) general academics (3) non-experts.
- Ask probing follow-up questions like a reviewer or committee member would.
- Use hedging phrases like "our results suggest", "this may indicate", "to the best of our knowledge".
- DO NOT correct mid-conversation. Model the correct form naturally.""",

    "business": """You are a business English conversation partner for a tech professional
preparing for job interviews and business meetings (湯凱傑, NUTC, graduating 2027-07).

Guidelines:
- Simulate realistic business scenarios: meetings, 1-on-1s, customer calls, interviews, negotiations.
- Use business idioms naturally ("circle back", "take it offline", "align expectations", "push back").
- Adapt register to the scenario (formal vs casual).
- Ask sharp follow-up questions like a hiring manager or business stakeholder.
- DO NOT correct mid-conversation. Model the correct form naturally.""",
}


FEEDBACK_PROMPT = """The conversation above just ended. The learner is 湯凱傑 (NUTC),
TOEIC 450 (L275/R175), targeting business English fluency by 2027-08.

Provide feedback in CHINESE (this is for HIS review, in his native language):

## 1. 最重要的 3 個錯誤
For each: (a) what he said, (b) why it's wrong / what's better, (c) the correct form.

## 2. 3 個他可以用得更地道的句塊
For each: (a) what he said (okay but plain), (b) a more idiomatic alternative.

## 3. 1 個值得加進 Anki 的句型
A sentence pattern he stumbled on or didn't know. Include:
- 句型 (English)
- 中文情境
- 2 個例句

## 4. 1 句話總結這次練習表現
（限 1 句，給他下一次更聚焦的方向）

Use markdown. Be specific, cite his actual words. Be encouraging but honest."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=list(MODE_PROMPTS.keys()),
        default="daily",
        help="Conversation mode (default: daily)",
    )
    parser.add_argument(
        "--no-log",
        action="store_true",
        help="Do not save conversation log",
    )
    return parser.parse_args()


def save_log(mode: str, messages: list[dict], feedback: str) -> Path:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = LOG_DIR / f"{ts}_{mode}.jsonl"
    with log_path.open("w", encoding="utf-8") as f:
        for m in messages:
            f.write(json.dumps({"role": m["role"], "content": m["content"]}, ensure_ascii=False) + "\n")
        f.write(json.dumps({"role": "feedback", "content": feedback}, ensure_ascii=False) + "\n")
    return log_path


def main() -> None:
    args = parse_args()

    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        print("  PowerShell: $env:ANTHROPIC_API_KEY = 'your-key-here'")
        sys.exit(1)

    client = Anthropic()
    system_prompt = MODE_PROMPTS[args.mode]

    print(f"\n English Speaking Practice — Mode: {args.mode}")
    print(" Type 'quit' to end and get feedback. Just talk naturally.\n")
    print("-" * 60)

    messages: list[dict] = []

    # Kickoff
    kickoff = "Hi! Let's have a short conversation. Greet me and ask me how my day is going."
    messages.append({"role": "user", "content": kickoff})
    response = client.messages.create(
        model=CHAT_MODEL,
        max_tokens=200,
        system=[{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}],
        messages=messages,
    )
    greeting = response.content[0].text
    messages.append({"role": "assistant", "content": greeting})
    print(f"\nPartner: {greeting}\n")

    # Conversation loop
    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n[interrupted]")
            break
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "bye", "stop"):
            break

        messages.append({"role": "user", "content": user_input})
        response = client.messages.create(
            model=CHAT_MODEL,
            max_tokens=300,
            system=[{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}],
            messages=messages,
        )
        reply = response.content[0].text
        messages.append({"role": "assistant", "content": reply})
        print(f"\nPartner: {reply}\n")

    if len(messages) < 4:
        print("\nConversation too short for feedback. Try again with more exchanges.")
        return

    # Feedback
    print("\n" + "=" * 60)
    print(" 📝 Generating feedback...")
    print("=" * 60 + "\n")

    feedback_messages = messages + [{"role": "user", "content": FEEDBACK_PROMPT}]
    feedback_response = client.messages.create(
        model=FEEDBACK_MODEL,
        max_tokens=1500,
        system="You are an experienced English teacher giving feedback to a Taiwanese learner. Reply in Chinese (Traditional).",
        messages=feedback_messages,
    )
    feedback = feedback_response.content[0].text
    print(feedback)

    if not args.no_log:
        log_path = save_log(args.mode, messages, feedback)
        print(f"\n Logged to: {log_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
