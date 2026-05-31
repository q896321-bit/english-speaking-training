# 訓練方法詳解

四大核心方法的細節說明。

---

## 1. Shadowing (影子跟讀)

### 是什麼
跟讀英文音檔，**落後原音 1-2 秒**，同步講出來。

### 為什麼有效
- 同步訓練「聽 + 講」迴路（傳統方法分開練）
- 強制模仿 **prosody** (重音、語調、連音)
- 無暇思考翻譯 → 強制建立直接英文路徑
- 自動修正你的「中式英語」韻律慣性

### 五遍法
1. **第 1 遍**: 純聽，不看字幕，抓大意
2. **第 2 遍**: 看字幕聽，對齊聽覺與文字
3. **第 3 遍**: 跟讀 0.75x（慢速跟讀）
4. **第 4 遍**: 跟讀原速（同步讀，看字幕）
5. **第 5 遍**: **影子跟讀** — 落後 1-2 秒，看字幕同步講

### 進度建議
- Stage 1: 1-min 短片（BBC 6 Minute）
- Stage 2: 3-min 學術片（TED-Ed, conference talks）
- Stage 3: 5-min 商業片（HBR podcast 段落）

### 推薦來源
| 等級 | 來源 | 為什麼 |
|---|---|---|
| 入門 | BBC 6 Minute English | 速度慢、字幕準、主題單一 |
| 中階 | TED-Ed | 5 分鐘、字幕、教育主題 |
| 中階 | VoiceTube | 中英對照、可重複跟讀 |
| 進階 | CVPR/ICCV Oral | 你領域，雙重收益 |
| 商業 | HBR IdeaCast | 商業詞彙、清楚發音 |

### 致命錯誤
- ✗ 只跟讀字面意思（沒抓韻律）
- ✗ 第一次就嘗試影子跟讀（要先聽熟）
- ✗ 選太難的音檔（>50% 字不會就太難）
- ✗ 沒錄音（聽不到自己的問題）

---

## 2. Sentence Chunks (句塊安裝)

### 是什麼
**預製的多字組合**，當作一個認知單位處理。例：
- "I was wondering if..." (一個 chunk, 不是 4 個字)
- "Let me get back to you" (一個 chunk)
- "Our results suggest that..." (一個 chunk)

### 為什麼有效
- 母語者口語 ~50% 是 formulaic chunks (Erman & Warren, 2000)
- 一個 chunk = 一個工作記憶 slot（而不是 5 個）
- 用 chunks 思考 → 工作記憶空出來做內容
- 訓練「直接英文構句」而非「中翻英」

### 安裝流程
1. **學習**: 看 chunk + 中文情境 + 例句
2. **內化**: Anki 卡片，每日複習
3. **產出**: 自己造 3 句話用這個 chunk
4. **使用**: 下一次 self-talk 故意用上

### Anki 卡片設計
```
正面: 中文情境 + 你想說的意思
範例: 「我在想要不要 X」
反面: I was wondering if I should X.
       + 你自己造的 3 個例句（手寫加進去）
```

### 致命錯誤
- ✗ 把 chunk 當單字背（要當 unit 內化）
- ✗ 學了不用（沒安裝到工作記憶）
- ✗ 一次貪多（每天 ≤5 個新 chunk）

---

## 3. Self-Talk (自我對話)

### 是什麼
**獨自用英文講話**——洗澡、走路、通勤、睡前。

### 為什麼有效
- 0 焦慮 → 繞過 Affective Filter (Krashen)
- 100% 練習時間（不像對話有 50% 時間在聽）
- 暴露你的構句缺口（Output Hypothesis - noticing）
- 大量重複 → 推到 procedural automaticity (DeKeyser)

### 黃金規則
1. **不停**: 卡住就用簡單句替代，絕不停下來查
2. **不查**: 卡住的詞記下來，self-talk 結束才查
3. **不譯**: 從英文意圖直接產出，不從中文翻
4. **重複**: 同一句話可以講 3 遍，越來越流暢

### 主題來源
- 早上: 今天計畫
- 中午: 早上做了什麼
- 晚上: 今天總結 + 明天計畫
- 走路: 看到的東西
- 洗澡: 抽 [`../drills/self-talk-prompts.md`](../drills/self-talk-prompts.md) 一題

### 進階: Self-talk + Recording
- 每週 ≥ 1 次錄音
- 重聽找 3 個改進點
- 標記重複錯誤 → 變成 Anki 卡

### 致命錯誤
- ✗ 覺得「自言自語很笨」放棄（那是 Affective Filter 在抵抗）
- ✗ 等到「準備好」才開始（永遠不會準備好）
- ✗ 中途停下查字典（破壞 flow，回到中翻英模式）

---

## 4. AI Conversation Partner (Claude)

### 是什麼
用 [`scripts/practice_partner.py`](../scripts/practice_partner.py) 跟 Claude 對話練習。

### 為什麼有效
- **無焦慮**: 不會被笑、不會等不及
- **無限耐心**: 你想練多久就多久
- **即時 feedback**: 對話結束有改進建議
- **可控難度**: --mode 參數控制等級
- **24/7 可用**: 半夜也能練

### 三種模式
- `--mode daily`: 日常對話（Stage 1）
- `--mode academic`: 學術對話（Stage 2，配合 CiI 投稿）
- `--mode business`: 商務對話（Stage 3，會議/簡報/面試）

### 使用方式
```powershell
python scripts/practice_partner.py --mode daily
```

對話完按 `quit` 結束，自動產生 feedback。

### 致命錯誤
- ✗ 完全靠 AI 取代真人練習（Stage 2 必須加入真人）
- ✗ 寫一段英文丟給 AI 改（那是寫作，不是口說）
- ✗ 完美主義（看到糾正就重打。Output Hypothesis: 錯誤是學習觸發點）

---

## 方法 × 階段對應

| 方法 | Stage 1 | Stage 2 | Stage 3 |
|---|---|---|---|
| Shadowing | 1-min daily | 3-min daily | 5-min business |
| Chunks | daily-80 | + academic-50 | + business-50 |
| Self-talk | 5 min daily | 10 min daily | 10 min daily |
| AI Partner | 1x/week | 2x/week | 3x/week |
| 真人對話 | 0 | iTalki 2x/week | iTalki 3x/week |

四個方法是**正交**的——每個訓練不同肌肉，不可互相替代。
