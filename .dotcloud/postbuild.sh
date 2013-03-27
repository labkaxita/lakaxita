cp ./.dotcloud/postinstall ./postinstall
cp ./.dotcloud/nginx.conf ./nginx.conf
mkdir -p /home/dotcloud/data/media /home/dotcloud/volatile/static
python bootstrap.py
./bin/buildout -c buildout.d/production.cfg -N
cp ./bin/django.wsgi ./wsgi.py
