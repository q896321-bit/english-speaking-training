# 前置作業 (Pre-flight Checklist)

Day 0 安裝，**最多花 2 小時**。Day 1 開始 routine。

---

## ✅ 必裝（一定要做完才能 Day 1）

### 電腦 (Windows)
- [ ] **Anki Desktop** — https://apps.ankiweb.net/
  - 下載 Windows 版，免費
  - 註冊 AnkiWeb 帳號（讓電腦↔手機同步）

- [ ] **Python 3.10+** — https://www.python.org/downloads/
  - 安裝時勾「Add to PATH」
  - 驗證: 開 PowerShell 打 `python --version`

- [ ] **Anthropic Python SDK**
  ```powershell
  pip install anthropic
  ```

- [ ] **API Key** — https://console.anthropic.com/
  - 註冊帳號 → API Keys → Create Key
  - 設環境變數（PowerShell）:
    ```powershell
    [Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-...", "User")
    ```
  - **重開 PowerShell 才生效**
  - 驗證: `$env:ANTHROPIC_API_KEY` 應印出 key

### 手機
- [ ] **AnkiDroid** (Android, 免費) — Google Play 搜尋
  - 或 **AnkiMobile** (iOS, $25 一次) — App Store
- [ ] **錄音 App**（系統內建即可）
  - 用於 self-talk 錄音與每週重聽
- [ ] **耳機 with 麥克風**（自我聽音、shadowing 用）

### 帳號註冊
- [ ] **AnkiWeb** (cloud sync) — https://ankiweb.net/account/register
- [ ] **YouTube** — 建立播放清單「English Shadowing」
- [ ] **(Stage 2 才需)** iTalki — https://www.italki.com/

---

## ✅ 強烈建議（不裝會多卡）

- [ ] **ELSA Speak** (發音 AI, 免費 tier 夠用)
  - https://elsaspeak.com/
  - 主要修個別單字發音（補 shadowing 不夠細的地方）

- [ ] **Linguee** Chrome 擴充 (查單字 + 雙語例句)
  - https://www.linguee.com/

- [ ] **VoiceTube** App (中英字幕影片)
  - https://tw.voicetube.com/

---

## ✅ Day 0 起點存證（30 分鐘）

走完安裝後做這 4 件事，記在 [`../logs/2026-05-31.md`](../logs/2026-05-31.md):

### 1. Anki 第一張卡 (5 min)
- 開 Anki → 新建 deck 叫 `english-speaking-training`
- 手動加 5 張 chunk 卡（從 [`../chunks/daily-80.md`](../chunks/daily-80.md) 抄前 5 個）
- 卡片格式：正面=中文情境，反面=English chunk

### 2. Shadowing 第一個書籤 (5 min)
- 開 BBC 6 Minute English: https://www.bbc.co.uk/learningenglish/english/features/6-minute-english
- 加書籤 + 挑最新一集，先聽一遍當作起點

### 3. 第一次 self-talk 錄音 (5 min)
- 手機錄音 App
- 題目: "Describe what you did today and your research, in English."
- 計時 1 分鐘，誠實錄（卡住也錄）
- **保存這支錄音** — 半年後你會聽自己的進步

### 4. Practice Partner 試跑 (10 min)
```powershell
cd C:\Users\KJ\english-speaking-training
python scripts/practice_partner.py --mode daily
```
- 對話 5 句就 `quit`
- 看 feedback 是否正常產生（驗證 API 通）

---

## ✅ 時間 blocking（決定就不變）

- [ ] **Daily 20 min 時段**: ___________ （例：早 7:00-7:20, 午休 12:30-12:50）
- [ ] 設手機 calendar 重複事件 + 提醒
- [ ] 加入家人/室友的告知（他們知道這時段你不被打擾）

---

## ✅ 心理準備

- [ ] 接受**前 4 週感覺沒進步**（acquisition is silent until threshold）
- [ ] 接受 self-talk 時看起來/聽起來笨（Affective Filter 在抵抗）
- [ ] 接受**錯誤是學習觸發點**（不是 bug）
- [ ] 給自己一個「失敗條款」: 中斷 1 天 OK，連續 3 天斷就停下重新評估

---

## 全部勾完？

開始 Day 1 → 跳到 [`../docs/01-stage1-survival.md`](../docs/01-stage1-survival.md) 的「每日 Routine」。
