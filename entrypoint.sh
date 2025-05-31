set -e

uv run python project/manage.py makemigrations

uv run python project/manage.py migrate

uv run python project/manage.py createsuperuser --noinput || true

uv run python project/manage.py runserver 0.0.0.0:8000