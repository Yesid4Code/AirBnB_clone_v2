#!/usr/bin/python3
"""
    Script that start a Flask web application
    listening on 0.0.0.0 port 5000.
"""
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ Closes sessions. """
    storage.close()


@app.route("/citiest_by_states", strict_slashes=False)
def states_and_cities():
    """ List all states and cities. """
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
