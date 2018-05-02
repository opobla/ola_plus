FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.txt /config/
RUN pip install --upgrade pip
RUN pip install -r /config/requirements.txt
RUN mkdir /local;
ADD /app /local
EXPOSE 8000
CMD bash -c "python manage.py makemigrations && python manage.py migrate && uwsgi --http :8000 --module ola_plus.wsgi:application"
WORKDIR /local
