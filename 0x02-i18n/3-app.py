#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask
from flask import render_template, request
from flask_babel import Babel


class Config:
    """ language config """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ selects local lang """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ return index template """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
