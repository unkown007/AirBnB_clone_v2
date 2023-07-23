#!/usr/bin/python3
""" starts a Flask web application """
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def rm_session(arg):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ display a HTML page """
    st = storage.all(State)
    if id is None:
        st = st.values()
        if st is not None:
            st = sorted(st, key=lambda state: state.name)
            return render_template('9-states.html', states=st)
    else:
        key = State.__name__ + '.' + id
        state = st.get(key)
        found = False
        if state is not None:
            state.cities = sorted(state.cities, key=lambda city: city.name)
            found = True

        return render_template('9-states.html', states=state, found=found)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
