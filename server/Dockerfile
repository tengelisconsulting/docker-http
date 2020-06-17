FROM openresty/openresty:buster-fat

WORKDIR /tmp

RUN opm get fffonion/lua-resty-openssl

ENV TINI_VERSION v0.19.0
RUN curl -L https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini -o /tini \
        && chmod +x /tini


WORKDIR /app

VOLUME /app/logs

COPY ./entrypoint.sh ./entrypoint.sh

COPY ./nginx ./nginx
COPY ./lua ./lua

ENTRYPOINT [ "/tini", "/app/entrypoint.sh" ]
