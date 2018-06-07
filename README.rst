cookiecutter-flask-api
======================

A Flask and REST api with swagger template for cookiecutter_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

.. image:: https://travis-ci.org/narfman0/cookiecutter-flask-api.svg
    :target: https://travis-ci.org/narfman0/cookiecutter-flask-api
    :alt: Build Status

Usage
-----
::

    $ pip install cookiecutter
    $ cookiecutter gh:narfman0/cookiecutter-flask-api

You will be asked about your basic info (name, project name, app name, etc.).
This info will be used in your new project. After generation, refer to the
README in the project :)

Features
--------

- ci support
- serverless template for cloud deploys and Procfile for deploying to a PaaS (e.g. Heroku)
- tox/pytest unit testing (example test included)
- api and swagger support

TODO
----

* End-to-end test serverless (looks right syntactically, did not test it)
* Make `cat` configurable
* Ensure coverage/reports work

LICENSE
-------

See accompanying LICENSE file for license information
