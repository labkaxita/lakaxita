[![Build Status](https://travis-ci.org/labkaxita/lakaxita.png)](https://travis-ci.org/labkaxita/lakaxita)

Lakaxita Gaztetxea's web page
=============================


Main components
===============

- buildout: build environment.
- django: backend web framework.
- django-modeltranslation: model translation.
- django-tastypie: public API.
- require.js: JS module loading.
- backbone.js: JS frontend framework.
- djangoembed: use and produce oembeds.

Optimizers and converters 
-------------------------

- django-require: r.js optimizer interface.
- yammy: python html to html converter.
- sass: sass to css converter.
- fontcustom: svg to font converter.


Installation
============

Development
-----------

    git clone https://github.com/labkaxita/lakaxita.git
    cd lakaxita
    python bootstrap.py
    aptitude install fontforge ttfautohint
    ./bin/buildout
    ./bin/django syncdb --migrate
    ./bin/django runserver


### Example data

It's very useful to load some example data in development. This data can be generated automagically but it's always better to have more realistic input:

    ./bin/django loaddata example_data.json

BTW, all the example photos are taken from flickr under a creative commons license and no modifications are intended.


### SASS to CSS compiler
    
    ./bin/sass-watch


### SVG to font conmpiler

    ./bin/font-watch


Deployment
----------

### Configuration
    git clone https://github.com/labkaxita/lakaxita.git
    cd lakaxita
    pip install dotcloud # system wide or virtualenv
    dotcloud setup # dotcloud user & pass
    dotcloud check
    dotcloud connect --git lakaxita

### Deploy
    # push latests git commits
    dotcloud push
