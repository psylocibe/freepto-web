import os

lang_dirs = sorted((d for d in
        os.listdir('templates/') if
        os.path.isdir(os.path.join('templates/', d))
        ))

def find_pages(lang):
    base = os.path.join('templates', lang)
    for f in os.listdir(base):
        if not f.endswith('.html'):
            continue
        if f == 'base.html' or f.startswith('_'):
            continue
        yield os.path.splitext(f)[0]

