
# 📡 Telegram Trading Signal Bot

This is an auto signal Telegram bot connected to TradingView via webhook. You can manually select trading pair and expiry time in Telegram, and receive automatic trading signals.

## ✅ Features
- Manual pair & expiry time selection
- Auto signals from TradingView via webhook
- Sends formatted signal messages to Telegram
- Supports Forex and OTC pairs
- Deployed easily on Railway (no credit card)

## 🧱 Files Included
- `bot.py` – Main Python code for the bot
- `requirements.txt` – Required libraries
- `README.md` – You are reading it now!

## 🚀 How to Deploy on Railway

1. **Upload this code to GitHub**
   - Create a new repo (e.g., `telegram-signal-bot`)
   - Upload `bot.py`, `requirements.txt`, and `README.md`

2. **Go to [https://railway.app](https://railway.app)**
   - Sign in with GitHub
   - Click **New Project > Deploy from GitHub Repo**

3. **Set Environment Variables**
   - `BOT_TOKEN`: Your Telegram bot token
   - `USER_ID`: Your Telegram user ID

4. **Your bot will run at:**
   ```
   https://<your-app-name>.up.railway.app/webhook
   ```

5. **TradingView Webhook Example:**
   - Webhook URL: The link above
   - Message (JSON):
     ```json
     {
       "direction": "Buy",
       "confidence": "85%",
       "entry": "1.23456"
     }
     ```

Enjoy accurate auto trading signals! 💹
