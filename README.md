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
- pyScss: scss to css converter.


Installation
============

Development
-----------

    git clone https://github.com/labkaxita/lakaxita.git
    cd lakaxita
    python bootstrap.py
    ./bin/buildout
    ./bin/django syncdb --migrate
    ./bin/django runserver


Deployment
----------

### Configuration
    pip install dotcloud
    dotcloud setup
    dotcloud check
    dotcloud connect --git www.0

### Deploy
    dotcloud push
