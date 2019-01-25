#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Invoke tasks."""
import os
import json
import shutil
from pathlib import Path

from invoke import task

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "cookiecutter.json"), "r") as fp:
    COOKIECUTTER_SETTINGS = json.load(fp)
# Match default value of app_name from cookiecutter.json
COOKIE = os.path.join(HERE, COOKIECUTTER_SETTINGS["app_name"])
APP = os.path.join(COOKIE, COOKIECUTTER_SETTINGS["app_name"], "app.py")


@task
def build(ctx):
    """Build the cookiecutter."""
    if Path(COOKIE).is_dir():
        print("Cookiecutter path already exists, skipping")
    else:
        ctx.run("cookiecutter {0} --no-input".format(HERE))


@task
def clean(ctx):
    """Clean out generated cookiecutter."""
    if os.path.exists(COOKIE):
        shutil.rmtree(COOKIE)
        print("Removed {0}".format(COOKIE))
    else:
        print("App directory does not exist. Skipping.")


@task(pre=[build])
def test(ctx):
    """Run lint commands and tests."""
    os.chdir(COOKIE)
    ctx.run("make test")
