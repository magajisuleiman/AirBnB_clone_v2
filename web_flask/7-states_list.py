#!/usr/bin/python3
''' Script that starts web application '''

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
''' flask app instance '''
app.url_map.strict_slashes = False


@app.teardown_appcontext
def flask_teardown(exc):
    ''' For removing the current SQLAlchemy Session'''
    storage.close()


@app.route('/states_list')
def Slist():
    ''' states list '''
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    stat = {
            'states': states
            }
    return render_template('7-states_list.html', **stat)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')
