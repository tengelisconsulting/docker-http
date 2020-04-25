FROM alpine:3.11

RUN apk --update --no-cache add \
        python3 \
        py-zmq \
        docker

WORKDIR /app

COPY ./py ./py

ENTRYPOINT [ "/app/py/main.py" ]
