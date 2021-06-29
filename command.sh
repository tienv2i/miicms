#!/bin/bash
echo "Waiting for postgres..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.1
done
    echo "PostgreSQL started"

# if [[ ! -f "install.lock" ]];
# then
#     # python Pillow-8.2.0/setup.py --install
#     # pip install ./cached/Pillow-8.2.0.tar.gz
#     # pip install ./cached/Django-3.2.4-py3-none-any.whl
#     pip install -r ./requirements.txt
#     touch install.lock
# fi


python manage.py makemigrations --no-input
python manage.py migrate --no-input
# python manage.py collectstatic --no-input
python init.py

if [[ "$DEBUG" == "True" ]];
then
    python manage.py runserver 0.0.0.0:8000
else
    gunicorn --bind :8000 miicms.wsgi:application
fi
