#!/usr/bin/python3

from flask import Flask, escape, request, abort, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def var(text):
    return "C " + text


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def setted(text="is cool"):
    text = text.replace("_", " ")
    return ('Python ' + text)


@app.route("/number/<n>", strict_slashes=False)
def integer(n):
    try:
        int(n)
        return (n + ' is a number')
    except:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def render(n):
    try:
        int(n)
        return render_template('5-number.html', n=n)
    except:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def renderooe(n):
    try:
        int(n)
        if n % 2 == 0:
            return render_template('6-number_odd_or_even.html',
                                   n=n,
                                   ooe='even')
        else:
            return render_template('6-number_odd_or_even.html',
                                   n=n,
                                   ooe='odd')
    except:
        abort(404)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
