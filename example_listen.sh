#!/usr/bin/env bash


on_url_match() {
    input=$1
    url=$2
    cb=$3
    if [[ "$(grep ${url} <<< ${input})" ]]; then
        ${cb} &
    fi
}


update_onward() {
    echo "UPDATING ONWARD BACKEND"
    cd /home/liam/projects/onward/backend
    git pull \
        && source ./env/prod.env \
        && docker-compose pull \
        && echo "y" | docker system prune \
        && docker-compose down --remove-orphans \
        && docker-compose up -d

}


while true; do
    echo "listening for work..."
    input=$(nc -l -p ${LOCAL_HOOK_PORT})
    on_url_match $input "/build-success/onward" update_onward
done
