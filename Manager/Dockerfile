FROM python:3.11

RUN mkdir /Manager

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/* \

COPY Manager/ /Manager/

RUN pip install -r /Manager/requirements.txt


WORKDIR /Manager

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
