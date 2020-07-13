#!/bin/sh


env_sub() {
    val=$(eval "echo \"\$$1\"")
    sed_arg="s/\\\${$1}/${val}/"
    sed -i -e $sed_arg nginx/nginx.conf
}


main() {
    set -e

    cp nginx/nginx.template.conf nginx/nginx.conf
    env_sub PORT
    env_sub LOCAL_HOOK_PORT

    openresty -p `pwd`/ -c nginx/nginx.conf

    tail -f logs/*.log
}


main
