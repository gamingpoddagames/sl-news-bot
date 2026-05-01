def get_news():
    try:
        if not NEWS_API.startswith("http"):
            return "⚠️ NEWS API not configured properly"

        res = requests.get(NEWS_API).json()
        articles = res.get("articles", [])[:5]

        msg = "🚨 SL BREAKING NEWS 24/7\n\n"

        for a in articles:
            msg += f"• {a.get('title')}\n{a.get('url')}\n\n"

        return msg

    except Exception as e:
        return f"Error fetching news: {str(e)}"
