FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system
RUN set -x \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
    build-essential libffi-dev libxml2-dev libxslt-dev libpq-dev \
    $(if [ "$DEVEL" = "yes" ]; then echo 'libjpeg-dev'; fi)
COPY . /code/