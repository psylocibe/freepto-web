from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
import re
import requests

from discovery import lang_dirs

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
    DEFAULT='en'
    return render_template('htaccess.html',
            languages=[(l,l) for l in lang_dirs if l != DEFAULT],
            default_dir=DEFAULT
            )

def render(lang, title):
    template = "%s/%s.html" % (lang, title)
    return render_template(template)


def get_images_data():
    base_url = 'http://download.freepto.mx/latest/'

    latest = requests.get(base_url)
    if latest.status_code != 200:
        raise Exception('Can\'t download http://download.freepto.mx/latest/')

    latest_text = latest.text.replace('\n', '')
    locales = re.findall('(freepto-[a-z]{2}_[A-Z]{2}_[\-0-9\.]*)', latest_text)

    images_data = {}
    for locale in locales:
        sha512_url = '%s/%s/%s.sha512sum.txt' % (base_url, locale, locale)
        sha512 = requests.get(sha512_url)
        if sha512.status_code != 200:
            raise Exception('Can\'t download %s' % sha512_url)

        images_data[locale] = {
            'http_download': '%s%s/%s.img' % (base_url, locale, locale),
            'torrent_download': '%s%s/%s.torrent' % (base_url, locale, locale),
            'sha512': sha512.text,
            'sha512sig': sha512_url + '.sig'
        }
    return images_data

app.jinja_env.globals.update(get_images_data=get_images_data)
