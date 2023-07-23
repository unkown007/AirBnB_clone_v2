#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display 'n is a number' only  if n is an integer
    Args:
        n(int): integer number
    Return: n is a number
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display a HTML page only if n is an integer
    Args:
        n(int): integer number to display
    Return: generated HTML page
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
	""" display a HTML page only if n is an integer
	Args:
		n(int): integer number
	Return: a HTML page
	"""
	return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    """ execute the app """
    app.run(host="0.0.0.0", port=5000)
