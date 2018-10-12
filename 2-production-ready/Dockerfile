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
