import requests
import time

BOT_TOKEN = "7964042596:AAERuaP19P5gpHdxNQxjVh-L9SCjYn6MGkU"
CHANNEL_ID = "8376417027"

NEWS_API = "https://newsapi.org/v2/top-headlines?country=us&apiKey=fc1399b9a22944cca99206c268a68a06"

def get_news():
    try:
        res = requests.get(NEWS_API).json()
        articles = res.get("articles", [])[:5]

        messages = []
        for a in articles:
            title = a["title"]
            url = a["url"]
            messages.append(f"🚨 {title}\n{url}")

        return "\n\n".join(messages)
    except:
        return "No news available right now."

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL_ID,
        "text": message
    }
    requests.post(url, data=data)

while True:
    news = get_news()
    send_telegram(news)
    time.sleep(3600)  # 1 hour
