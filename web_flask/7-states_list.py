#!/usr/bin/python3
""" starts Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def state_list():
    """ Displays HTML page """
    return render_template("7-states_list.html",
                           data=storage.all(State).values())


@app.teardown_appcontext
def storage_close(var=None):
    """closes running session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
