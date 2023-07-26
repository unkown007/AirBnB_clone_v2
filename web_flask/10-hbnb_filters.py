#!/usr/bin/python3
""" starts a Flask web application """
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def err(error):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """ display a HTML page like 6-index.html """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    if states is not None:
        states = sorted(states, key=lambda state: state.name)
        for state in states:
            if state.cities is not None:
                state.cities = sorted(
                        state.cities, key=lambda city: city.name)

    if amenities is not None:
        amenities = sorted(states, key=lambda amenity: amenity.name)

    return render_template(
            '10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
