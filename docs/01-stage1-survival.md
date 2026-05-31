# Stage 1: Survival (Month 1-3)

**期間**: 2026-06-01 ~ 2026-08-31
**目標**: TOEIC 450 → 600 / 從「無法構句」到「能構句」
**每日預算**: 20 分鐘

---

## 每日 Routine（4 blocks × 5 min = 20 min）

### Block A: Shadowing (5 min)

**來源**:
- BBC 6 Minute English (主要)
- VoiceTube short clips
- TED 1-min teasers

**5 遍法**:
1. 只聽，不看字幕（抓大意）
2. 看字幕聽（對齊認知）
3. 跟讀，0.75x 慢速
4. 跟讀，原速
5. **影子跟讀**：落後 1-2 秒，看字幕同步講

**重點**: 模仿語調起伏（prosody），不是逐字念對。**錄音第 5 遍**，每週日聽自己一週前的錄音對比。

### Block B: Anki Chunks (5 min)

- 來源: [`../chunks/daily-80.md`](../chunks/daily-80.md)
- 每日新增: 3-5 個 chunk（不要貪心）
- 每日複習: 系統推送的卡片
- 卡片格式:
  ```
  正面: 我在想可不可以...（情境）
  反面: I was wondering if I could...
  ```

### Block C: Self-talk (5 min)

**環境**: 走路 / 洗澡 / 通勤（**低焦慮，無人聽**）

**規則**:
- 主題: 今天做了什麼 + 用今天學的 chunks
- 不要停下來查字典
- 不會就用簡單句替代
- 卡住的詞記下來，晚上查

**示範**:
> "Today I worked on my thesis. I was wondering if my G3a method needs more ablations. The results suggest that hard union works best. I think I'll add McNemar tests this week."

### Block D: 朗讀論文 (5 min)

- 來源: 你 thesis 的 Related Work 段落（每天一段）
- 大聲朗讀，每段念 2 遍
- **為什麼有效**: 你已經理解內容 → 大腦不必處理意義 → 全部資源給發音與韻律

---

## 每週 Routine

### 週一 ~ 週六: Daily routine + 加碼
- **週三 (+15 min)**: Claude practice partner 對話
  ```powershell
  python scripts/practice_partner.py --mode daily
  ```
- **週六 (+30 min)**: 寫 100 字英文日記（昨天 + 今天 + 明天）

### 週日: Review Day
- 填 [`../drills/weekly-template.md`](../drills/weekly-template.md)
- 檢查 Anki retention（目標 >85%）
- 規劃下週的 self-talk 主題
- 聽上週的 shadowing 錄音，自評

---

## Week-by-Week 進度

### Week 1-2: 安裝基礎設施
- 設定 Anki，匯入 `daily-80.md` 前 20 個 chunks
- 找 5 個 shadowing 來源（書籤）
- Day 1: 錄第一次 self-talk（基準線存證）

### Week 3-4: 開始累積
- Anki 累積: 40 chunks
- 第二週末: 第一篇 100 字英文日記

### Week 5-8: 加速
- Anki 累積: 60 chunks
- 加入 Claude practice partner（每週 1 次）
- Week 6: 第一次 TOEIC mini-test

### Week 9-12: 收尾與評估
- Anki 累積: 80 chunks 全部安裝
- Week 11: 完整 TOEIC 模擬考
- Week 12: 決定是否進入 Stage 2

---

## 常見障礙與對策

| 障礙 | 對策 |
|---|---|
| 「我今天累，跳過一天」 | 砍到 5 分鐘，但**不能斷**。連續性 > 強度 |
| 「不會說某個東西」 | 用簡單句繞過。記下來，晚上查。**Self-talk 中絕不停** |
| 「Anki 卡片越積越多」 | 每天最多新增 5 個。複習優先 |
| 「我覺得沒進步」 | 看 log + TOEIC 模擬分數。**感覺不準** |
| 「找不到 shadowing 來源」 | BBC 6 Minute English 是最穩起點 |
| 「Self-talk 覺得很笨」 | 那是 Affective Filter 在抵抗。每次做完記 1 句進步點 |

---

## 退出條件（必須全部達成）

進入 Stage 2 前要過：

- [ ] 80 個 daily chunks 全部 Anki retention >90%
- [ ] 可以 30 秒內生 5 句描述今天的英文（**錄音為證**）
- [ ] TOEIC 模擬考 ≥ 550
- [ ] 累計 self-talk 時間 ≥ 30 小時
- [ ] 連續每日 log ≥ 80 天（允許 1 週 1 天空檔）
