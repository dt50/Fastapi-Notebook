FROM python:3.8-alpine

ADD ./app /home/app/
WORKDIR /home/app/
ADD ./requirements.txt requirements.txt


ENV PYTHONPATH=${PYTHONPATH:-../}

RUN apk add --no-cache make postgresql-dev gcc musl-dev tree

RUN pip install --upgrade pip setuptools && \
    pip install -r ./requirements.txt


EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]