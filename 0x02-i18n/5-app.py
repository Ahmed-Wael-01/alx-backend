#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask
from flask import render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    if request.args.get('locale'):
        if request.args.get('locale') in app.config['LANGUAGES']:
            return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ get user id from url """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """ find user before any function """
    usr = get_user()
    if usr is not None:
        g.user = usr


@app.route('/')
def index():
    """ return index template """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
