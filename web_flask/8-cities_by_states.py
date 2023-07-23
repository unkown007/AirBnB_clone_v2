#!/usr/bin/python3
""" start a Flask web application """
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def rm_session(arg):
    """ remove the current Session """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities():
    """ display a HTML page """
    states = storage.all(State).values()
    if states is not None:
        states = sorted(states, key=lambda state: state.name)
        for state in states:
            if state.cities is not None:
                state.cities = sorted(
                        state.cities, key=lambda city: city.name)

    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    """ run the web app """
    app.run(host="0.0.0.0", port=5000)
