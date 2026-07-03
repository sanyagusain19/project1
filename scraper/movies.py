import requests

API_KEY = "83306ba2"

def fetch_movie(movie_name):
    if not movie_name:
        return None

    url = f"https://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"

    try:
        res = requests.get(url, timeout=5)
        data = res.json()

        if data.get("Response") == "True":
            return {
                "title": data.get("Title"),
                "year": data.get("Year"),
                "rating": data.get("imdbRating"),
                "genre": data.get("Genre"),
                "director": data.get("Director"),
                "runtime": data.get("Runtime"),
                "awards": data.get("Awards"),
                "plot": data.get("Plot"),
                "poster": data.get("Poster"),
            }

        return None

    except:
        return None