from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.config['DEBUG'] = True
Bootstrap(app)

@app.route('/')
def index():
    return render('it', 'index')

@app.route('/<lang>/')
def page_index(lang):
    return render(lang, 'index')

@app.route('/<lang>/<title>/')
def page(lang, title):
    return render(lang, title)

@app.route('/.htaccess')
def htaccess():
    return render_template('htaccess.html',
            languages=(('it', 'it'), ('es', 'es')),
            default_dir='en'
            )

def render(lang, title):
    template = "%s/%s.html" % (lang, title)
    return render_template(template)
