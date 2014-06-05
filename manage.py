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
    yield {'lang':'en'}

@freezer.register_generator
def page():
    yield {'lang':'it', 'title':'usa_freepto'}
    yield {'lang':'it', 'title':'contatti'}
    yield {'lang':'it', 'title':'dev-team'}
    yield {'lang':'it', 'title':'doc-team'}
    yield {'lang':'it', 'title':'testing-team'}
    yield {'lang':'it', 'title':'eventi'}
    yield {'lang':'it', 'title':'download'}
    yield {'lang':'it', 'title':'news'}

    yield {'lang':'es', 'title':'usa_freepto'}
    yield {'lang':'es', 'title':'contactos'}
    yield {'lang':'es', 'title':'dev-team'}
    yield {'lang':'es', 'title':'doc-team'}
    yield {'lang':'es', 'title':'testing-team'}
    yield {'lang':'es', 'title':'eventos'}
    yield {'lang':'es', 'title':'noticias'}
    yield {'lang':'es', 'title':'descargas'}

    yield {'lang':'en', 'title':'get-started'}
    yield {'lang':'en', 'title':'get-in-touch'}
    yield {'lang':'en', 'title':'dev-team'}
    yield {'lang':'en', 'title':'doc-team'}
    yield {'lang':'en', 'title':'testing-team'}
    yield {'lang':'en', 'title':'events'}
    yield {'lang':'en', 'title':'download'}
    yield {'lang':'en', 'title':'news'}

@manager.command
def freeze():
    freezer.freeze()

if __name__ == "__main__":
    manager.run()
