#!/usr/bin/python3
"""
 A script that starts a flask web application
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import state

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_bnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python/')
@app.route('/python/<text>')
def Python_text(text='is cool'):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def num(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def num_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    ''' definition '''
    if n % 2 == 0:
        num = 'even'
    else:
        num = "odd"
    return render_template('6-number_odd_or_even.html', number=n, parity=num)

@app.route('/states_list')
def states_list():
    """ def doc """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    """ def doc """
    storage.close()

@app.route('/cities_by_states')
def cities_by_states():
    """ def doc """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)

@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    """ Route function for /states and /states/<id> """
    not_found = False
    if id is not None:
        states = storage.all(State, id)
        with_id = True
        if len(states) == 0:
            not_found = True
    else:
        states = storage.all(State)
        with_id = False
    return render_template('9-states.html', states=states,
                           with_id=with_id, not_found=not_found)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
