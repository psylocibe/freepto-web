freepto-web
===========

Flask scripts for Freepto's website.

HTML generation
===============

To generate the HTML for the website, use this command:

    make all

HTML generation (manual mode)
=============================
You shouldn't need to do this, but if for some reason you cannot use `make` or if it is broken, then you can build the HTML manually.

Static HTML files will be created in the `build` subdirectory.

    # create virtualenv:
    virtualenv env
    
    # activate:
    source env/bin/activate
    
    # install requirements:
    pip install -r requirements.txt
    
    # freeze new version:
    python manage.py freeze
