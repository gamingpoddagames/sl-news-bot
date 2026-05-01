import os
import requests

NEWS_API = os.environ["NEWS_API"]

print("NEWS API:", NEWS_API)

res = requests.get(NEWS_API)
print("STATUS:", res.status_code)
print("RESPONSE:", res.text[:500])
