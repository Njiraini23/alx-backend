#!/usr/bin/env python3
"""a flask application"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


def get_user() -> Union[Dict, None]:
    """returns a user dictionary or
    None if the ID cannot be found or if login_as was not passed"""
    user_id = request.args.get('login_as', None)
    if user_id is not None and int(user_id) in users.keys():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """ find a user if any, and set it as a global on flask.g.user"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """return best language match based on supported languages"""
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    if g.user:
        loc = g.user.get('locale')
        if loc and loc in app.config['LANGUAGES']:
            return loc
    loc = request.headers.get('locale', None)
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """configure timezone"""
    user_tz = None
    parameter_tz = request.args.get("timezone")
    if parameter_tz:
        try:
            user_tz = pytz.timezone(parameter_tz)
        except pytz.UnknownTimeZoneError:
            raise pytz.UnknownTimeZoneError

    if not user_tz and g.user and g.user.get("timezone"):
        try:
            user_tz = pytz.timezone(g.user.get("timezone"))
        except pytz.UnknownTimeZoneError:
            raise pytz.UnknownTimeZoneError

    return user_tz or Config.BABEL_DEFAULT_TIMEZONE


@app.route('/', strict_slashes=False)
def index() -> str:
    """for the / route"""
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
