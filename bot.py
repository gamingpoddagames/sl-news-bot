import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ["CHANNEL"]
NEWS_API = os.environ["NEWS_API"]

def get_news():
    res = requests.get(NEWS_API).json()
    articles = res.get("articles", [])[:5]

    msg = "🚨 SL BREAKING NEWS 24/7\n\n"

    for a in articles:
        title = a.get("title")
        url = a.get("url")
        msg += f"• {title}\n{url}\n\n"

    return msg

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHANNEL,
        "text": msg
    })

send(get_news())
