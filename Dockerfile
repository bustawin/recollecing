FROM python:3.7.5-slim-buster AS base
WORKDIR /app
COPY ./setup.py ./
COPY ./requirements.txt ./
COPY ./README.rst ./
RUN pip install -e . -r requirements.txt
# COPY ./ ./ # Overriden with docker-compose's volume
EXPOSE 80
ENV DB_URI change-this-in-docker-compose

FROM base as test
# todo make tests auto-run on changes
CMD python setup.py test

FROM base as devel
ENV FLASK_APP ./product_scraper/app.py
CMD flask run -p 80 -h 0.0.0.0
