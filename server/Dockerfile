FROM openresty/openresty:buster-fat

WORKDIR /tmp

RUN opm get fffonion/lua-resty-openssl

RUN apt update \
        && apt install --assume-yes \
        build-essential \
        unzip \
        wget \
        libzmq3-dev

RUN wget http://luarocks.org/releases/luarocks-2.0.13.tar.gz \
        && tar -xzvf luarocks-2.0.13.tar.gz \
        && cd luarocks-2.0.13/ \
        && ./configure --prefix=/usr/local/openresty/luajit \
        --with-lua=/usr/local/openresty/luajit/ \
        --lua-suffix=jit \
        --with-lua-include=/usr/local/openresty/luajit/include/luajit-2.1

RUN cd luarocks-2.0.13 \
        && make \
        && make install

RUN /usr/local/openresty/luajit/bin/luarocks install lzmq

WORKDIR /app

VOLUME /app/logs

COPY ./entrypoint.sh ./entrypoint.sh

COPY ./nginx ./nginx
COPY ./lua ./lua

ENTRYPOINT [ "/app/entrypoint.sh" ]
