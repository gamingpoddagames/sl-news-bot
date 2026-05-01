import requests

BOT_TOKEN = "7964042596:AAERuaP19P5gpHdxNQxjVh-L9SCjYn6MGkU"
CHANNEL_USERNAME = "@newssl247_bot"

NEWS_API = "https://newsapi.org/v2/top-headlines?country=us&apiKey=fc1399b9a22944cca99206c268a68a06"

def get_news():
    res = requests.get(NEWS_API).json()
    articles = res.get("articles", [])[:5]

    message = "🚨 *SL BREAKING NEWS 24/7*\n\n"

    for a in articles:
        title = a.get("title", "No title")
        url = a.get("url", "")
        message += f"• {title}\n{url}\n\n"

    return message

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL_USERNAME,
        "text": msg,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=data)

if __name__ == "__main__":
    send(get_news())
