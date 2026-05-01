import os
import requests

BOT_TOKEN = os.environ["7964042596:AAERuaP19P5gpHdxNQxjVh-L9SCjYn6MGkU"]
CHANNEL = os.environ["@slnews247"]

NEWS_API = os.environ["fc1399b9a22944cca99206c268a68a06"]

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

if __name__ == "__main__":
    send(get_news())
