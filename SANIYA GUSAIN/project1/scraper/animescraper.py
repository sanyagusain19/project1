import requests
from bs4 import BeautifulSoup
def anime_scraper():
    headers = {"User-Agent": "Mozilla/5.0"}

    url = f"https://myanimelist.net/topanime.php?limit=0"
    response = requests.get(url, headers)
    response.status_code
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    a =soup.find_all('tr', class_ = 'ranking-list')
    anime_data = []

    for row in a:

        length = row.find_all("span", class_="bookstore-price")

        anime = {
        "rank": row.find("span", class_="top-anime-rank-text").text.strip(),
        "title": row.find("h3", class_="anime_ranking_h3").text.strip(),
        "score": row.find("td", class_="score").text.strip(),
        "url": row.find("a", class_="hoverinfo_trigger").get("href"),
        "book_price": length[0].text.strip() if len(length) > 0 else "N/A"
        }

        anime_data.append(anime)
    return anime_data