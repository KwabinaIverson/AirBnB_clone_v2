#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000, and has two routes:
- /: displays "Hello HBNB!"
- /hbnb: displays "HBNB"

The option strict_slashes=False is used in the route definitions.
"""

from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" when the root route is accessed.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" when the /hbnb route is accessed.
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def show_variable(text):
    """
    Display "C" followed by the varible
    """
    return f'C {escape(text)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
