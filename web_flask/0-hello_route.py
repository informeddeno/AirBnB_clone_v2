#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ returns Hello HBNB! """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
