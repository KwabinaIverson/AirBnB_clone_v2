#!/usr/bin/python3
"""
Module: 7-cities_by_states
Web application with Flask that displays a list of states and cities.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(error):
    """Closes the database connection at the end of the request."""
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """
    Display an HTML page with a list of states and cities.

    Fetches data from the storage engine (FileStorage or DBStorage).

    If the storage engine is DBStorage, it uses the 'cities' relationship.
    Otherwise, it uses the public getter method 'cities'.
    """
    states = storage.all("State").values()
    states_sorted = sorted(states, key=lambda x: x.name)

    return render_template('7-states_list.html', states=states_sorted)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
