#!/usr/bin/python3
"""
This script starts a Flask web application with specific routes.

Web application listens on 0.0.0.0, port 5000.
Routes:
- /: display "Hello HBNB!"
- /hbnb: display "HBNB"
- /c/<text>: display "C ", followed by the value of the text variable (replace underscore _ symbols with a space)
- /python/(<text>): display "Python ", followed by the value of the text variable (replace underscore _ symbols with a space)
  Default value of text is "is cool".
- /number/<n>: display "n is a number" only if n is an integer
Uses the option strict_slashes=False in route definitions.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" on the main route.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" on the /hbnb route.
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays "C ", followed by the value of the text variable.
    Replaces underscores with spaces.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text='is_cool'):
    """
    Displays "Python ", followed by the value of the text variable.
    Replaces underscores with spaces. Default value is "is cool".
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Displays "n is a number" only if n is an integer.
    """
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
