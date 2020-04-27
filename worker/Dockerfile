FROM alpine:3.11

RUN apk --update --no-cache add \
        python3 \
        py-zmq \
        docker

RUN python3 -m pip install \
        PyYAML==5.3.1

WORKDIR /app

COPY ./py ./py

ENTRYPOINT [ "/app/py/main.py" ]
