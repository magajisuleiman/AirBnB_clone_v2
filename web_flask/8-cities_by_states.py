#!/usr/bin/python3
'''Flask web app'''

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
'''Flask app instance.'''
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    '''cities_by_states route'''
    allstates = list(storage.all(State).values())
    allstates.sort(key=lambda x: x.name)
    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    dictss = {
        'states': allstates
    }
    return render_template('8-cities_by_states.html', **dictss)


@app.teardown_appcontext
def flask_teardown(exc):
    '''flask teardown '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
