## Go to Project path
cd /path/to/ola_plus

## Create the virtualenv with name *env*
virtualenv -p python3 env

## Activate the virtualenv
source env/bin/activate

## Install the dependencies
pip install -r requirements.txt

## Create the local.py settings for development
echo "from .base import *" > ola_plus/settings/local.py

## Migrate the models
python manage.py migrate --settings=ola_plus.settings.local

## Load existing fixtures
python manage.py fixtureloader --settings=ola_plus.settings.local

## Run development Server
python manage.py runserver --settings=ola_plus.settings.local