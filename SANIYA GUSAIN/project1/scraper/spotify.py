import requests
from bs4 import BeautifulSoup
def spotify():
    url = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    info = soup.find_all('div',  class_="IJBqrvvMtwQ258xS")
    spotify_data = []

    for artist in info:

        artist_tag = artist.find("a", class_="izvk_EbfhLUCNE6Q")

        if artist_tag:

            spotify = {

                "artist_name": artist_tag.text.strip(),

                "artist_link": artist_tag.get("href")

            }

            spotify_data.append(spotify)

    return spotify_data