#!/usr/bin/python3
""" Script that start a Flask web application on 0.0.0.0 port 5000. """
from flask import Flask
app = Flask(__name__)
app.url_map.stric_slashes = False


@app.route('/')
def hello_world():
    """ . """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
