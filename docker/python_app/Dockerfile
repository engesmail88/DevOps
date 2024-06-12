FROM python:alpine

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000

