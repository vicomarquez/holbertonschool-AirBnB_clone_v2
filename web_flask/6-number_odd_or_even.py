#!/usr/bin/python3
"""displays a text variable"""


from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def txt(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
