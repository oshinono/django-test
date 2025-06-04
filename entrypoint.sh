set -e

uv run python project/manage.py makemigrations

uv run python project/manage.py migrate

uv run python project/manage.py createsuperuser --noinput || true
uv run python project/manage.py collectstatic --noinput --clear

uv run gunicorn src.wsgi:application --config project/src/gunicorn_config.py --chdir project