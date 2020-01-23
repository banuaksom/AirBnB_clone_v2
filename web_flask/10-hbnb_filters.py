#!/usr/bin/python3
""" starts Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def states():
    """ displays HTML page """
    return render_template("10-hbnb_filters.html",
                           location=storage.all(State).values(),
                           amenities=storage.all(Amenity).values())


@app.teardown_appcontext
def storage_close(var=None):
    """ closes running session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
