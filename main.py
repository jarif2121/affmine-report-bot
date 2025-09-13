import requests

url = "https://api.telegram.org/bot8314345509:AAFfdLoRpJGXweYrQnhem6Y_ffGIsgCOc4o/sendMessage"
payload = {
    "chat_id": "-1002980195580",
    "text": "🖥 : CpaFull_Dashboard 🇧🇩\n\n🙎 : {aff_sub}\n💰 : {payout}\n🎁 : {offer_name}\n📶 : {conversation}\n⏱️ : {datetime}\n🆘 : {ip}\n\n🌼 Alahamdulillah 🌼"
}

requests.post(url, data=payload)
