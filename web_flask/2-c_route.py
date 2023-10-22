#!/usr/bin/python3
''' SCript that starts flask web application '''

from flask import Flask

app = Flask(__name__)
''' flask app instance created '''
app.url_map.strict_slashes = False


@app.route('/')
def greet():
    ''' say hello hbnb '''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    ''' say hbnb '''
    return "HBNB"


@app.route('/c/<text>')
def show(text):
    ''' say c and some text '''
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
