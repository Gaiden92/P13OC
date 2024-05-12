set -0 errexit
exec pip install -r requirements.txt
exec python ./manage.py collectstatic --no-input
exec python ./manage.py migrate
exec ./manage.py runserver "0.0.0.0:8000"