===============================
{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.project_short_description}}


Quickstart
----------

Bootstrap using pipenv::

    git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
    cd {{cookiecutter.app_name}}
    pipenv install; pipenv shell

Using inferior manual venv ::

    git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
    cd {{cookiecutter.app_name}}
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt

In general, before running shell commands, set the ``FLASK_APP`` and
``FLASK_DEBUG`` environment variables ::

    export FLASK_APP={{ cookiecutter.app_name }}.app
    export FLASK_DEBUG=1

To run app::

    flask run

Then you may navigate the following url: `localhost:5000/api/v1/`. Hurrah!

Running Tests
-------------

To run all tests, run ::

    tox

LICENSE
-------

See accompanying LICENSE file for license information
