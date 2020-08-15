import re
import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://timesofindia.indiatimes.com/")

soup = bs(r.text, "html.parser")
results = soup.find("div", {"data-vr-zone": "headlines"})
item = results.find("a", attrs={'href': re.compile("^/")})
link = item.get("href")
title = item.get("title")
print(link)
print(title)
