./.dotcloud/createdb.py
./.dotcloud/mkadmin.py
./bin/django syncdb --migrate --noinput
./bin/django collectstatic --noinput
