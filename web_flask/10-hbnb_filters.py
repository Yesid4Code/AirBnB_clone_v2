#!/usr/bin/python3
"""
    Script that start a Flask web application
    listening on 0.0.0.0 port 5000.
"""
from flask import Flask, render_template
from models.amenity import Amenity
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ Closes sessions. """
    storage.close()



@app.route("/hbnb_filters", strict_slashes=False)
def states_id(id=None):
    """ List all states and cities. """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
