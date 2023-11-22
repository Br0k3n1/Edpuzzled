FROM python:slim

RUN pip install --upgrade pip \
    && mkdir /app
WORKDIR /app

COPY ./src/ /app/
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/app/main.py"]