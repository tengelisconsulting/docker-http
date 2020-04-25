FROM openresty/openresty:buster-fat

WORKDIR /app

RUN opm get fffonion/lua-resty-openssl

VOLUME /app/logs

COPY ./entrypoint.sh ./entrypoint.sh

COPY ./nginx ./nginx
COPY ./scripts ./scripts
COPY ./lua ./lua

ENTRYPOINT [ "/app/entrypoint.sh" ]
