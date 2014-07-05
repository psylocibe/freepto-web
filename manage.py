#!/usr/bin/env python

from flask.ext.script import Manager
from flask_frozen import Freezer
from app import app
import discovery
manager = Manager(app)

freezer = Freezer(app)

@freezer.register_generator
def index():
    yield {}

@freezer.register_generator
def page_index():
    for lang in discovery.lang_dirs:
        yield {'lang': lang}

@freezer.register_generator
def page():
    for lang in discovery.lang_dirs:
        for title in discovery.find_pages(lang):
            yield {'lang': lang, 'title': title}

@manager.command
def freeze():
    freezer.freeze()

if __name__ == "__main__":
    manager.run()
