python bootstrap.py
./bin/buildout -c production.cfg -N
cp ./bin/django.wsgi ./wsgi.py
./.dotcloud/createdb.py
./.dotcloud/mkadmin.py
./bin/django syncdb --migrate --noinput
mkdir -p /home/dotcloud/data/media /home/dotcloud/volatile/static
./bin/django collectstatic --noinput
