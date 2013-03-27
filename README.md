[![Build Status](https://travis-ci.org/labkaxita/lakaxita.png)](https://travis-ci.org/labkaxita/lakaxita)

Lakaxita Gaztetxea's web page
=============================


Development mode installation
----------------------------

    git clone https://github.com/labkaxita/lakaxita.git
    cd lakaxita
    python bootstrap.py
    ./bin/buildout -c devel.cfg
    ./bin/django syncdb --migrate
    ./bin/django runserver


Configure dotcloud
------------------

    pip install dotcloud
    dotcloud setup
    dotcloud check
    dotcloud connect --git www.0


Push commits to dotcloud
------------------------

    dotcloud push
