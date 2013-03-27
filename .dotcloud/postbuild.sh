cp ./.dotcloud/postinstall ./postinstall
cp ./.dotcloud/nginx.conf ./nginx.conf
mkdir -p /home/dotcloud/data/media /home/dotcloud/volatile/static
sed -i 's/development/production/g' buildout.cfg
python bootstrap.py
./bin/buildout
cp ./bin/django.wsgi ./wsgi.py
