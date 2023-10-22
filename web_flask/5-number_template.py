#!/usr/bin/python3
''' Scripts that starts flask web applicaiton '''

from flask import Flask, render_template
from markupsafe import escape

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


@app.route('/c/<text>')
def cshow(text):
    ''' shows c and some text '''
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def show(text):
    ''' shows python and some text '''
    if (text):
        return f"Python {text.replace('_', ' ')}"
    else:
        return "Python is cool"


@app.route('/number/<int:n>')
def number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def showint(n):
    return render_template('5-number.html', num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
