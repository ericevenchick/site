from flask import Flask, render_template
from flask.ext.assets import Environment
from flask.ext.markdown import Markdown
from argh import *

app = Flask(__name__)
assets = Environment(app)
markdown = Markdown(app)

# Configuration
DEBUG = True        # enable debugging mode

# Flask Routing

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# CLI Commands

@command
def serve(server="127.0.0.1", port=8080, debug=DEBUG):
    """ Start a server to run the site
        default: 127.0.0.1:8080
    """
    app.run(host=server, port=port, debug=debug)

if __name__ == "__main__":
    parser = ArghParser()
    parser.add_commands([serve,])
    parser.dispatch()
