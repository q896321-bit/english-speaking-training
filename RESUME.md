# 下次回來從這裡開始

最後一次更新: Day 0 setup 進行中

---

## ✅ 已完成（不用再做）

- Anki Desktop 已裝（舊安裝，profile「使用者 1」）
- Python 路徑確認: **`C:\Users\KJ\anaconda3\python.exe`** (Python 3.13.9, SSL OK)
- anthropic SDK 0.105.2 已裝
- Anki 第一批匯入檔生成: `anki-import/daily-80-first5.txt`
- 專案推上 GitHub: https://github.com/q896321-bit/english-speaking-training
- prerequisites doc 加入專屬 Python 路徑備註

### 系統環境注意 (避免再踩同樣坑)
- ❌ `python` (PATH) → Windows Store 偽 stub，**不可用**
- ❌ `py` 啟動器 → `C:\ProgramData\Anaconda3`，**SSL 模組壞掉**
- ✅ 真正可用: `C:\Users\KJ\anaconda3\python.exe`

---

## ⏳ 下次回來要做的 3 件事（不要超過 30 分鐘）

### 1. API Key 設定

開 https://console.anthropic.com/settings/keys → Create Key → 複製。

在 PowerShell 跑（把 sk-ant-... 換成你的 key）：
```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-貼你的key", "User")
```

**關掉這個 PowerShell 視窗，重開一個新的**（環境變數要新視窗才生效）。

驗證:
```powershell
$env:ANTHROPIC_API_KEY.Length  # 應該印一個三位數
```

### 2. Anki 第一個 deck

1. 開 Anki Desktop
2. 主畫面 **Create Deck** → 命名 `english-speaking-training`
3. **File → Import** → 選 `C:\Users\KJ\english-speaking-training\anki-import\daily-80-first5.txt`
4. 確認 Type=Basic, Deck=english-speaking-training, 用 Tab 分隔
5. Deck Options → New cards/day = **5**

### 3. BBC 6 Minute English 書籤

開 https://www.bbc.co.uk/learningenglish/english/features/6-minute-english → **Ctrl+D 加書籤** → 點最新一集確認有 transcript + MP3。

---

## 🔒 跟下次的 Claude 說

> 「我做完 RESUME.md 的 3 件事了，繼續跑 prerequisites checklist」

Claude 會：
1. 驗證 API Key 有設好
2. 跑 `practice_partner.py` smoke test（3 句對話）
3. 推進手機 AnkiDroid 安裝 + Day 0 baseline 自我錄音
4. 全部勾完 → 進 Day 1 routine（明天 2026-06-02 開始）

---

## 待辦清單檢視

剩下的前置作業:
- [ ] API Key 取得 + 設環境變數
- [ ] Anki 建 deck + 匯入 5 張卡
- [ ] BBC 加書籤 + 挑第一集
- [ ] `practice_partner.py` smoke test
- [ ] 手機 AnkiDroid (Android) 或 AnkiMobile (iOS)
- [ ] Day 0 baseline self-talk 錄音 1 分鐘
- [ ] 決定每日 20 min 固定時段
- [ ] (選配) ELSA Speak 安裝

Day 1 routine 開始日期: **2026-06-02**
