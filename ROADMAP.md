# 18-Month Roadmap

對齊畢業時程（2027-07）。每個階段有量化指標和退出條件。

---

## Stage 1: Survival (2026-06-01 ~ 2026-08-31, 3 個月)

**入場**: TOEIC 450, 無法構句
**目標**: TOEIC 600, 可在 30 秒內說出 5 句連貫英文
**時間預算**: 20 min/day, 7 天/週

### 每日 Routine
- 5 min: Shadowing (1-min clip × 5 reps)
- 5 min: Anki 10 chunks (新增 3-5 + 複習)
- 5 min: Self-talk (用今天的 chunks 講今天做了什麼)
- 5 min: 朗讀自己論文 Related Work 一段

### 每週 Routine
- 1 × 100 字英文日記
- 1 × 15-min Claude practice partner 對話 (`scripts/practice_partner.py --mode daily`)
- 週日: 填寫 weekly review (`drills/weekly-template.md`)

### 退出條件（必須全部達成才進 Stage 2）
- [ ] 80 個 daily chunks 全部 Anki retention >90%
- [ ] 30 秒內生出 5 句描述今天的英文（錄音證明）
- [ ] TOEIC 模擬考 ≥ 550
- [ ] 累計 self-talk 時間 ≥ 30 小時
- [ ] 連續每日 log ≥ 80 天（允許 1 週 1 天空檔）

---

## Stage 2: Fluency (2026-09-01 ~ 2027-02-28, 6 個月)

**入場**: TOEIC 550-600, 能簡短表達
**目標**: TOEIC 750, 能 10-min 對話、能做論文 oral pitch
**時間預算**: 30-40 min/day

### 每日 Routine
- 10 min: Shadowing (3-min academic talk: TED-Ed / CVPR oral)
- 5 min: Anki (加入 `academic-50.md` 句塊)
- 10 min: Self-talk on topic（從 `self-talk-prompts.md` 抽 1 題）
- 5 min: 論文段落英文初稿（**不要中翻英**）

### 每週 Routine
- 2 × 30-min iTalki tutor OR 語言交換
- 1 × 5-min 錄音 monologue + 自我檢討
- 1 × 朗讀 1 篇 conference paper

### 退出條件
- [ ] `academic-50.md` chunks 全部熟練
- [ ] 可以做 5 分鐘論文 pitch（無稿，錄影為證）
- [ ] TOEIC 模擬考 ≥ 720
- [ ] 累計英文字寫作 ≥ 10,000（論文 + 日記）
- [ ] CiI 投稿前，論文全英文初稿至少 1 輪自寫（不靠中翻英）

---

## Stage 3: Business English (2027-03-01 ~ 2027-08-31, 6 個月)

**入場**: TOEIC 700+
**目標**: TOEIC 850+, 商務會議、面試、簡報無障礙
**時間預算**: 45-60 min/day

### 每日 Routine
- 15 min: Business podcast (HBR IdeaCast / A16Z) + shadowing
- 10 min: `business-50.md` chunks 練習
- 10 min: 商務 role-play with Claude (`--mode business`)
- 10 min: Email/Slack 英文寫作

### 每週 Routine
- 1 × Mock meeting (Claude or human)
- 1 × 90-second elevator pitch (錄影 + 檢討)
- 1 × Case study reading + verbal summary

### 退出條件
- [ ] `business-50.md` chunks 自動化
- [ ] 15-min thesis defense in English mock 已通過 3 次
- [ ] TOEIC 模擬考 ≥ 830
- [ ] 可以即興 cold-call 一個英文 conference Q&A
- [ ] 一次英文面試經驗（實習 / 工作 / mock）

---

## 量化追蹤指標（每月底計算）

填入 `logs/monthly-tracker.md`：

- 累計 shadowing 時數 (target: 30 hr/month by Stage 3)
- Anki retention rate (target: >85%)
- Self-talk 累計時數
- 估算輸出句數 (self-talk min × ~3 sentences/min)
- TOEIC 模擬考分數 (季度測一次)

---

## 為什麼是 18 個月？

CEFR 學習時數研究：
- A2 → B1: 150-200 小時
- B1 → B2: 200-300 小時
- B2 → C1: 300-400 小時
- **Total A2 → C1: 600-900 小時**

18 個月 × 平均 1 hr/day = 540 hr，加上週末加碼 ~700 hr，落在 **B2 上緣 / C1 下緣**（TOEIC 800-850 區間 = 商用英語起點）。

時間是不可壓縮的。沒有捷徑，只有複利。
