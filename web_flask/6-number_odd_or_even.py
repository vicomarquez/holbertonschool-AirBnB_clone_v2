#!/usr/bin/python3
"""Start web application with two routings
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    """Return string when route queried
    """
    strict_slashes = False
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string when route queried
    """
    strict_slashes = False
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Return reformatted text
    """
    strict_slashes = False
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Reformat text based on optional variable
    """
    strict_slashes = False
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """Allow request if path variable is a valid integer
    """
    strict_slashes = False
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """Retrieve template for request
    """
    path = '5-number.html'
    strict_slashes = False
    return render_template(path, n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Render template based on conditional
    """
    path = '6-number_odd_or_even.html'
    strict_slashes = False
    return render_template(path, n=n)

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
