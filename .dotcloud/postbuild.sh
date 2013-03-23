cp ./.dotcloud/postinstall ./postinstall
python bootstrap.py
./bin/buildout -c production.cfg -N
cp ./bin/django.wsgi ./wsgi.py
mkdir -p /home/dotcloud/data/media /home/dotcloud/volatile/static
