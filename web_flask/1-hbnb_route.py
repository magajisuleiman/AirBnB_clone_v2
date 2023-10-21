#!/usr/bin/python3
''' Scripts that starts flask web applicaiton '''

from flask import Flask

app = Flask(__name__)
''' Flask app instance '''
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    ''' the route says hello '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    ''' the route says show hbnb '''
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
