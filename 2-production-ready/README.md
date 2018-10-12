# A production ready http

## Building Docker image

The Python 3 based [Dockerfile](Dockerfile) uses an Alpine Linux base image
and expects the application source code to be volume mounted at `/application`
when run:

```
FROM python:3.6.1-alpine
ADD . /application
WORKDIR /application
RUN addgroup -S flaskgroup && adduser -S -G flaskgroup flask && \
    chown -R flask:flaskgroup /application
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install -r app/requirements.txt; \
	apk del .build-deps;
EXPOSE 5000
VOLUME /application

CMD uwsgi --ini app.ini
```

The last statement shows how we are running the application via `uwsgi`.
We define the `wsgi` configuration in a self-contained manner by 
creating the `app.ini`.  

To build the image:

```
$ docker build -t webapp -f Dockerfile .
```


## Bringing up the web application, along with prometheus

The [docker-compse.yml](docker-compose.yml) brings up the `webapp` 
service which is our web application
using the image `webapp` we built above. 
The [docker-compose.yml](docker-compose.yml)
file brings up the `statsd` service which is 
the statsd exporter, `prometheus` service and also starts the `grafana` service which
is available on port 3000.
We introduced the `nginx` web server for web serving, 
reverse proxying, caching, load balancing the web application.
We also added in the `docker-compose.yml` file the `restart: always` rule, 
to restart the application on crash.   
The developer can easily switch between environment 
by changing the environment variable in the `docker-compose.yml` file.

To bring up all the services:

```
$ docker-compose -f docker-compose.yml --build up
```

