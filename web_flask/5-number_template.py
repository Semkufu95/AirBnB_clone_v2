#!/usr/bin/python3
"""
 A script that starts a flask web application
"""

from flask import Flask
from flask import render_template

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
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
