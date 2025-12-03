#!/usr/bin/env bash
set -euo pipefail

# run_local.sh
# Usage: from the `moncv` folder (the folder that contains `manage.py`)
#   ./run_local.sh
# Optional env vars for non-interactive superuser creation:
#   DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

echo "Using project root: $ROOT_DIR"

if [ ! -d ".venv" ]; then
  echo "Creating virtualenv .venv..."
  python3 -m venv .venv
fi

echo "Activating virtualenv..."
. .venv/bin/activate

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing requirements..."
pip install -r requirements.txt -r backend/requirements.txt

echo "Running migrations..."
python manage.py migrate

if [ -n "${DJANGO_SUPERUSER_USERNAME:-}" ] && [ -n "${DJANGO_SUPERUSER_EMAIL:-}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
  echo "Creating Django superuser non-interactively..."
  export DJANGO_SUPERUSER_PASSWORD
  python manage.py createsuperuser --noinput || true
else
  echo "To create a superuser non-interactively set DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL and DJANGO_SUPERUSER_PASSWORD"
fi

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec .venv/bin/gunicorn --chdir "$ROOT_DIR" moncv.wsgi:application --bind 0.0.0.0:8000 --workers 3
