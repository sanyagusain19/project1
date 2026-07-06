from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def streamgames():

    url = "https://store.steampowered.com/search/?filter=popularnew"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    games = soup.find_all('a', class_="search_result_row")      # Replace with your game's parent container

    games_data = []

    for game in games:

        game_name = game.find(
            "span",
            class_="title"
        ).get_text(strip=True)

        price = game.find(
            "div",
            class_="discount_final_price"
        ).get_text(strip=True)

        release = game.find(
            "div",
            class_="search_released"
        ).get_text(strip=True)

        image = game.find("img")

        image_url = urljoin(
            url,
            image.get("src")
        ) if image else "N/A"

        games_data.append({

            "game_name": game_name,

            "price": price,

            "release": release,

            "image_url": image_url

        })

    return games_data