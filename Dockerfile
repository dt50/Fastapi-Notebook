FROM alpine:3.7

ADD ./app /home/app/
WORKDIR /home/app/
ADD ./requirements.txt requirements.txt

ENV PYTHONPATH=${PYTHONPATH:-../}

RUN apk add --no-cache make postgresql-dev gcc python3 python3-dev musl-dev tree && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    pip3 install -r ./requirements.txt

RUN pwd && ls && tree
RUN cd $PYTHONPATH && pwd && tree

EXPOSE 8000

ENTRYPOINT ["python3", "api/db/schemas/main.py"]