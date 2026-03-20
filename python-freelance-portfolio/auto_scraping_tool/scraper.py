import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_SITE = "http://books.toscrape.com/"

def parse_rating(class_list):
    rating_map = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
    for c in class_list:
        if c in rating_map:
            return rating_map[c]
    return 0

def fetch_books(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    for item in soup.select(".product_pod"):
        title = item.h3.a["title"]
        price_text = item.select_one(".price_color").text
        price = float(re.sub(r"[^\d.]", "", price_text))
        availability = item.select_one(".availability").text.strip()
        rating = parse_rating(item.p["class"])
        link = urljoin(BASE_SITE, item.h3.a["href"])

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "link": link
        })

    return books