#!/usr/bin/python3
"""
    Script that start a Flask web application
    listening on 0.0.0.0 port 5000.
"""
from flask import Flask
app = Flask(__name__)
app.url_map.stric_slashes = False


@app.route("/")
def display_hello():
    """ Display a message. """
    return "Hello HBNB!"


@app.route("/hbnb")
def display_hbnb():
    """ Display a message. """
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """ . """
    return ("C {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
