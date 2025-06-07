python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn finals.wsgi --log-file -