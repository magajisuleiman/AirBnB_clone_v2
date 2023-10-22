#!/usr/bin/python3
'''starts Flask web application'''

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
'''the app instance.'''
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    '''states page route'''
    state = None
    states = None
    allstates = list(storage.all(State).values())
    case = 404
    if id is not None:
        res = list(filter(lambda x: x.id == id, allstates))
        if len(res) > 0:
            state = res[0]
            state.cities.sort(key=lambda x: x.name)
            case = 2
    else:
        states = allstates
        for state in states:
            state.cities.sort(key=lambda x: x.name)
        states.sort(key=lambda x: x.name)
        case = 1
    dictss = {
        'states': states, 'state': state, 'case': case
    }
    return render_template('9-states.html', **dictss)


@app.teardown_appcontext
def flask_teardown(exc):
    '''the flask teardown'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
