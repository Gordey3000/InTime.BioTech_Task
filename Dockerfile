
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Biotech

COPY . /Biotech/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y postgresql-client

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000