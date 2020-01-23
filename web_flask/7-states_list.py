#!/usr/bin/python3
""" starts Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """ Displays HTML page
        H1 tag: “States”
        UL tag: list of all State objects
    """
    return render_template("7-states_list.html",
                           data=storage.all(State).values())


@app.teardown_appcontext
def storage_close(var=None):
    """closes running session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
