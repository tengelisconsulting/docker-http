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
    LOCKFILE="/tmp/onward.lock"
    cleanup() {
        rm -f "${LOCKFILE}"
    }
    trap cleanup SIGINT SIGTERM EXIT ERR
    if [[ -f "${LOCKFILE}" ]]; then
        echo "ONWARD UPDATE IN PROGRESS, WILL NOT ATTEMPT"
        return
    fi
    touch "${LOCKFILE}"
    echo "UPDATING ONWARD BACKEND"
    cd /home/liam/projects/onward/backend
    git pull \
        && source ./env/prod.env \
        && docker-compose pull \
        && echo "y" | docker system prune \
        && docker-compose down --remove-orphans \
        && docker-compose up -d
    cleanup
}

listen() {
    echo "listening at ${LOCAL_HOOK_PORT}..."
    input=$(nc -l -p ${LOCAL_HOOK_PORT})
    on_url_match $input "/build-success/onward" update_onward
}


main() {
    if [[ "${LOCAL_HOOK_PORT}" == "" ]]; then
        echo "set LOCAL_HOOK_PORT"
        exit 1
    fi
    while true; do
        listen
    done
}

main
