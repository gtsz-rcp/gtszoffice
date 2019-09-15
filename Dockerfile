FROM python:3.7.4

COPY . /app
WORKDIR /app

RUN apt-get -y update && apt-get install -y libzbar-dev
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]