import re
import requests
from win10toast import ToastNotifier
from bs4 import BeautifulSoup as bs

try:
    r = requests.get("https://timesofindia.indiatimes.com/")
except:
    r = None
    print("Check your internet connection")

if r is not None:
    soup = bs(r.text, "html.parser")
    results = soup.find("div", {"data-vr-zone": "headlines"})
    item = results.find("a", attrs={'href': re.compile("^/")})
    link = item.get("href")
    message = item.get("title")
    title = "Breaking news"

    toaster = ToastNotifier()
    toaster.show_toast(title, message, icon_path=r'C:\Users\Dell\Downloads\toi.ico', duration=10)
