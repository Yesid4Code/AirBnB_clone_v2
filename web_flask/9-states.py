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


@app.route("/states/", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """ List all states and cities. """
    states = None
    states_dic = storage.all(State)
    state_id = "State.{}".format(id)
    if state_id in states_dic.keys():
        states = states_dic[state_id]
    return render_template("9-states.html", states=states,
                           id=id, states_dic=states_dic)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
