FROM ubuntu:latest
MAINTAINER Kristin Aliberto "rugbychix@gmail.com"
RUN apt-get update -y
RUN apt-get update && apt-get install -y python \
	python-setuptools python-dev build-essential  \
	python-virtualenv \
	nginx gunicorn \
	supervisor \
	libffi-dev \
	libssl-dev \
	libmysqlclient-dev
RUN easy_install pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

#Copy Code
# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY config/nginx/ /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
RUN mkdir -p /var/log/supervisord
COPY config/supervisord/ /etc/supervisor/conf.d/

#this will help with server side scripts
WORKDIR /app
# Start processes
CMD ["/usr/bin/supervisord"]