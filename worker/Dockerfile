FROM alpine:3.11 AS base

RUN apk --update --no-cache add \
        python3 \
        py-zmq \
        docker

RUN python3 -m pip install \
        PyYAML==5.3.1

FROM base
RUN apk add --update \
        build-base \
        python3-dev
RUN python3 -m pip install mypy
COPY ./py ./py
RUN python3 -m mypy --ignore-missing-imports ./py

FROM base

WORKDIR /app
COPY ./py ./py

ENTRYPOINT [ "/app/py/main.py" ]
