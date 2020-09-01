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
    """ Display a message from a file. """
    return ("C {}".format(text.replace("_", " ")))


@app.route("/python/")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """ Display a message from a file. """
    return ("Python {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>")
def is_number(n):
    """ Display a message if the parameter is a number."""
    return ("{} is a number".format(n))


@app.route("/number_template/<init:n>")
def number_template(n):
    """ Display a HTML page if n is a number.
            H1 tag: Number: n inside the tab body
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
