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


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """ List all states and cities. """
    states = storage.all(State).values()
    if id:
        id = "State.{}".format(id)
        if id in states.keys():
            state = states[id]
    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
