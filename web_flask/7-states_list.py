#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def rm_session(arg):
    """ remove the current SQLAlchemy Session """
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states():
    """ display a HTML page """
    st = storage.all(State).values()
    if st is not None:
        st = sorted(st, key=lambda state: state.name)
    return render_template('7-states_list.html', states=st)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
