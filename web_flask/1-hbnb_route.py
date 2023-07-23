#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ print hello world when requested / """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ print HBNB when requested /hbnb """
    return "HBNB"


if __name__ == "__main__":
    """ execute the app """
    app.run(host="0.0.0.0", port=5000)
