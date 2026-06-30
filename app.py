from flask import Flask, render_template
app = Flask(__name__)  #contains main 
print(__name__)

@app.route("/")
def home():
    return render_template ("home.html")

@app.route("/about")
def about():
    return render_template ("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/webscraping")
def webscraping():
    return render_template("webscraping.html")

@app.route("/staticscraping")
def staticscraping():
    return render_template("staticscraping.html")


if (__name__ == "__main__"):
    app.run(host = "0.0.0.0", port = 5000, debug = True)  # host, port are optional, change in file server restart ->debug = true
    