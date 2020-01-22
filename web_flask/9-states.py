#!/usr/bin/python3
""" starts Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states():
    """ Displays HTML page """
    return render_template("9-states.html",
                           data=storage.all(State).values())


@app.route("/states/<id>")
def states_id(id=None):
    """ Displays HTML page """
    return render_template("9-states.html",
                           data=storage.all(State).values(),
                           id=id)


@app.teardown_appcontext
def storage_close(var=None):
    """closes running session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
