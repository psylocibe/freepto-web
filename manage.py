from flask.ext.script import Manager
from flask_frozen import Freezer
from app import app
manager = Manager(app)

freezer = Freezer(app)

@freezer.register_generator
def index():
    yield {}

@freezer.register_generator
def page_index():
    yield {'lang':'it'}
    yield {'lang':'es'}

@freezer.register_generator
def page():
    yield {'lang':'it', 'title':'usa_freepto'}
    yield {'lang':'it', 'title':'contatti'}
    yield {'lang':'it', 'title':'faq'}
    yield {'lang':'it', 'title':'dev-team'}
    yield {'lang':'it', 'title':'doc-team'}
    yield {'lang':'it', 'title':'testing-team'}

    yield {'lang':'es', 'title':'usa_freepto'}
    yield {'lang':'es', 'title':'contactos'}
    yield {'lang':'es', 'title':'faq'}
    yield {'lang':'es', 'title':'dev-team'}
    yield {'lang':'es', 'title':'doc-team'}
    yield {'lang':'es', 'title':'testing-team'}

@manager.command
def freeze():
    freezer.freeze()

if __name__ == "__main__":
    manager.run()
