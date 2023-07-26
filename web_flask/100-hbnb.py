#!/usr/bin/python3
""" starts a Flask web application """
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def err(error):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def filters():
    """ display a HTML page like 6-index.html """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User).values()
    if states is not None:
        states = sorted(states, key=lambda state: state.name)
        for state in states:
            if state.cities is not None:
                state.cities = sorted(
                        state.cities, key=lambda city: city.name)

    if amenities is not None:
        amenities = sorted(states, key=lambda amenity: amenity.name)

    if places is not None:
        places = sorted(places, key=lambda place: place.name)

        user_place = []
        for place in places:
            tmp = {}
            for user in users:
                if user.id == place.user_id:
                    tmp['id'] = user.id
                    tmp['name'] = user.first_name + ' ' + user.last_name
                    tmp['place'] = place
                    user_place.append(tmp)

    return render_template('100-hbnb.html', states=states, amenities=amenities, places=user_place)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
