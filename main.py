from flask import Flask, request
import requests

app = Flask(name)

TELEGRAM_BOT_TOKEN = "8314345509:AAFfdLoRpJGXweYrQnhem6Y_ffGIsgCOc4o"
CHAT_ID = "-1002980195580"

def format_message(data):
    aff_sub = data.get("aff_sub", "N/A")
    payout = data.get("payout", "N/A")
    offer_name = data.get("offer_name", "N/A")
    conversation = data.get("conversation", "N/A")
    datetime = data.get("datetime", "N/A")
    ip = data.get("ip", "N/A")

    message = (
        f"🖥 : CpaFull_Dashboard 🇧🇩\n\n"
        f"🙎 : {aff_sub}\n"
        f"💰 : {payout}\n"
        f"🎁 : {offer_name}\n"
        f"📶 : {conversation}\n"
        f"⏱️ : {datetime}\n"
        f"🆘 : {ip}\n\n"
        f"🌼 Alahamdulillah 🌼"
    )
    return message

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    text = format_message(data)
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload)
    return "OK", 200

@app.route('/')
def home():
    return "Bot is running", 200
