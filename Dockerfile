FROM python:3.9

RUN pip install --upgrade pip

WORKDIR app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . . 
