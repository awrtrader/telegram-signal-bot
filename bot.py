
import telebot
from flask import Flask, request
import os

# === CONFIG ===
BOT_TOKEN = os.environ.get("BOT_TOKEN")
USER_ID = os.environ.get("USER_ID")  # Your Telegram ID (for control)
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# === VARIABLES ===
selected_pair = {}
selected_expiry = {}

# === START ===
@bot.message_handler(commands=['start'])
def start(message):
    if str(message.chat.id) != USER_ID:
        bot.send_message(message.chat.id, "Access denied.")
        return
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📈 Forex", "🕒 OTC")
    bot.send_message(message.chat.id, "Choose Market Type:", reply_markup=markup)

# === PAIR SELECTION ===
@bot.message_handler(func=lambda m: m.text in ["📈 Forex", "🕒 OTC"])
def select_market(message):
    pairs = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCHF"] if "Forex" in message.text else ["OTC-EURUSD", "OTC-USDJPY"]
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for pair in pairs:
        markup.row(pair)
    bot.send_message(message.chat.id, "Choose your pair:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text in ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCHF", "OTC-EURUSD", "OTC-USDJPY"])
def choose_pair(message):
    selected_pair[message.chat.id] = message.text
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("5s", "15s", "30s")
    bot.send_message(message.chat.id, f"Selected Pair: {message.text}\nNow select expiry:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text in ["5s", "15s", "30s"])
def choose_expiry(message):
    selected_expiry[message.chat.id] = message.text
    bot.send_message(message.chat.id, f"✅ Pair: {selected_pair[message.chat.id]}\n⏱ Expiry: {message.text}\n\nBot is ready for signals.")

# === WEBHOOK (TradingView Sends Here) ===
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    direction = data.get("direction", "Buy")
    confidence = data.get("confidence", "80%")
    entry = data.get("entry", "1.23456")

    for chat_id in selected_pair:
        pair = selected_pair[chat_id]
        expiry = selected_expiry.get(chat_id, "15s")
        message = f"""📡 *Trading Signal*
        
📊 Pair: `{pair}`
📈 Direction: *{direction}*
⏱ Expiry: `{expiry}`
💰 Entry: `{entry}`
🔒 Confidence: *{confidence}*

#Binary #Signal"""
        bot.send_message(chat_id, message, parse_mode="Markdown")

    return "OK", 200

# === RUN FLASK ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
