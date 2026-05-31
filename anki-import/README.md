# Anki 匯入指南

## Day 0: 第一次匯入

### Step 1: 開 Anki Desktop
- 啟動 Anki，登入你的 AnkiWeb 帳號

### Step 2: 建立新 Deck
1. 主畫面點 **「Create Deck」**
2. 名稱: `english-speaking-training`
3. 確認

### Step 3: 匯入第一批 5 張卡
1. 主選單 → **File → Import**
2. 選 `daily-80-first5.txt`（本資料夾）
3. 匯入設定:
   - **Type**: Basic
   - **Deck**: `english-speaking-training`
   - **Fields separated by**: Tab
   - **Allow HTML in fields**: 否（檔案 header 會自動設定）
   - **Field 1 → Front (情境)**
   - **Field 2 → Back (English chunk)**
   - **Field 3 → Tags**
4. 按 **Import**

### Step 4: 設定每日卡數
1. 點 deck → **Options**
2. **New cards/day**: 5
3. **Maximum reviews/day**: 200
4. **Learning steps**: `1m 10m`
5. **Graduating interval**: 1 day

### Step 5: 試做一次 review
- 回主畫面 → 點 deck 名 → **Study Now**
- 看到中文情境（正面）→ 心中說英文 → 翻面對答
- **不要只是看懂**，要**講出聲音**

---

## 之後的批次

我會幫你陸續產生：
- `daily-80-batch2.txt` (chunks 6-20)
- `daily-80-batch3.txt` (chunks 21-40)
- etc.

或你也可以自己根據 `chunks/daily-80.md` 編輯 TSV 檔。

格式 (用 Tab 分隔):
```
中文情境	English chunk	tag1 tag2
```
