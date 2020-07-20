FROM alpine:3.7

ADD ./api /home/api/
WORKDIR /home/api/
ADD ./requirements.txt requirements.txt


RUN apk add --no-cache make postgresql-dev gcc python3 python3-dev musl-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    pip3 install -r ./requirements.txt

EXPOSE 8000

ENTRYPOINT ["python3", "main.py"]