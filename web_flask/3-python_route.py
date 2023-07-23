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


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ display 'C' followed by the value of the text variable
    (replace underscore _ symbols with a space)
    Args:
        text(str): text
    Return: C followed by text
    """
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ Display Python, followed by the value of text variable
    (replace underscore _ symbols with a symbols with a space)
    for requestes coming from /python/text
    Args:
        text(str): text to print
    Return: Python followd by text
    """
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == "__main__":
    """ execute the app """
    app.run(host="0.0.0.0", port=5000)
