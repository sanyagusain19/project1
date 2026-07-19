from flask import Flask, render_template, request, send_from_directory
import json
app = Flask(__name__)  #contains main 


from scraper.spotify import spotify
from scraper.topcompanies import top_companies_scraper
from scraper.animescraper import anime_scraper
from scraper.streamgames import streamgames
from scraper.goodreadsscraper import goodreads
from api.plants import fetch_plants, fetch_plant_detail
from scraper.movies import fetch_movie
from api.weather import fetch_weather
from api.pokemon import fetch_pokemon
from api.product import fetch_products
from dynamic.topcharts import fetch_top_movies
from dynamic.startup import fetch_startups
from dynamic.hackernews import fetch_hackernews
from dynamic.top_songs import fetch_top_songs
from dynamic.disasters import fetch_disasters

@app.route("/")
def home():
    return render_template ("home.html")
@app.route("/github")
def github_page():
   return render_template("github.html")

@app.route("/about")
def about():
    return render_template ("about.html")
@app.route("/journey")
def journey():
    return render_template("journey.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/webscraping")
def webscraping():
    return render_template("webscraping.html")

@app.route("/staticscraping")
def staticscraping():
    return render_template("staticscraping.html")
@app.route("/topcompaniesscraper")
def topcompaniesscraper():
    with open("companies_data.json", "r", encoding="utf-8") as f:
        companies = json.load(f)
    return render_template("topcompaniesscraper.html", companies=companies)
@app.route("/download/topcompanies")
def download_topcompanies_data():
    return send_from_directory(
        "one.ipynb",
        "topcompanies",     
        as_attachment=True
    )

@app.route("/animescraper")
def animescraper():
    animes = anime_scraper()
    
    return render_template("animescraper.html", animes = animes)
@app.route("/download/animes")
def download_animes_data():
    return send_from_directory(
        "one.ipynb",
        "anime",     
        as_attachment=True
    )


@app.route("/spotifyscraper")
def spotifyscraper():
    spotify_data = spotify()
    return render_template("spotify.html", spotify_data = spotify_data)


@app.route("/download/spotify")
def download_spotify():
    return send_from_directory(
        "one.ipynb",
        "Spotify_data",     
        as_attachment=True
    )

@app.route("/steamgamesscraper")
def steamgames():
    games_data = streamgames()
    return render_template("steamgames.html", games_data = games_data)

@app.route("/download/stream_games")
def download_stream_games():
    return send_from_directory(
        "one.ipynb",
        "stream_games",     
        as_attachment=True
    )

@app.route("/goodquotesscraper")
def quotes():
    quote_data = goodreads()
    
    return render_template("goodquotesscraper.html", quote_data = quote_data)
                           
@app.route("/download/goodreads")
def download_goodreads():
    return send_from_directory(
        "one.ipynb",
        "goodreads",     
        as_attachment=True
    )
   
@app.route("/apis")
def apis():
    return render_template("apis.html")

@app.route("/plants")
def plants():
    query = request.args.get("q")
    return render_template(
        "plants.html",
        data=fetch_plants(query) if query else None,
        query=query
    )
@app.route("/movies")
def movies():
    query = request.args.get("q")
    return render_template(
        "movies.html",
        data=fetch_movie(query) if query else None,
        query=query
    )
@app.route("/weather")
def weather():
    # lat = request.args.get("lat",type=float,default = 30.13)
    # lon = request.args.get("lon",type= float,default = 77.28)
    weather_data = fetch_weather(lat=30.13, lon=77.28)
    return render_template("weather.html", weather=weather_data)

@app.route("/pokemon")
def pokemon():
    name = request.args.get("name", type=str)

    pokemon_data = None
    if name:
        pokemon_data = fetch_pokemon(name)

    return render_template("pokemon.html", name=name, pokemon_data=pokemon_data)

@app.route("/products")
def products():
    products = fetch_products()
    return render_template("product.html", products=products)

@app.route("/dynamic")
def dynamicscraper():
    return render_template("dynamic_scraper.html")

@app.route("/dynamic/topcharts")
def topcharts():
    movies = fetch_top_movies()
    return render_template("topcharts.html", movies=movies[:25])

@app.route("/startup")
def startup():
    startups = fetch_startups()
    return render_template("startups.html", startups=startups)
@app.route("/hackernews")
def hackernews():
    news = fetch_hackernews()
    return render_template("hackernews.html", news = news)

@app.route("/topS")
def topS():
    top_songs = fetch_top_songs()
    return render_template("top_songs.html", songs = top_songs)
@app.route("/disasters")
def disasters():
    data = fetch_disasters()
    return render_template("disasters.html", disasters=data)

@app.route("/minorprojects")
def minorprojects():
    return render_template("minorprojects.html")

@app.route("/minor/churn")
def churn_project():
    return render_template("minor/index.html")
@app.route("/powerbi")
def powerbi():
    return render_template("powerbi.html")
@app.route("/music")
def music_page():
    return render_template("music.html")


if (__name__ == "__main__"):
    app.run(host = "0.0.0.0", port = 5000, debug = True)  # host, port are optional, change in file server restart ->debug = true
    