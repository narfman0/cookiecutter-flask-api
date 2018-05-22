# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask, render_template

from {{ cookiecutter.app_name }} import api


def create_app():
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_blueprints(app):
    app.register_blueprint(api.blueprint, url_prefix='api/1')


def register_errorhandlers(app):
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


if __name__ == "__main__":
    create_app()
