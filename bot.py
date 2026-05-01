import feedparser

def get_news():
    feed = feedparser.parse("https://feeds.bbci.co.uk/news/world/rss.xml")

    msg = "🚨 SL BREAKING NEWS 24/7\n\n"

    for entry in feed.entries[:5]:
        msg += f"• {entry.title}\n{entry.link}\n\n"

    return msg
