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


### SASS -> CSS converter
    
    ./bin/sass-watch


### SVG -> font converter

#### Installation

    wget http://people.mozilla.com/~jkew/woff/woff-code-latest.zip
    unzip woff-code-latest.zip -d sfnt2woff && cd sfnt2woff && make && \
    su -c  'mv sfnt2woff /usr/local/bin/' && cd .. && \
    rm -r woff-code-latest.zip sfnt2woff

#### Usage

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
