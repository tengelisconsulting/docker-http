#!/usr/bin/env bash


on_url_match() {
    input=$1
    url=$2
    cb=$3
    if [[ "$(grep ${url} <<< ${input})" ]]; then
        ${cb} &
    fi
}


test_handler() {
    echo "this is the test handler"
    sleep 2
    echo "done my work"
}

while true; do
    input=$(nc -l -p ${LOCAL_HOOK_PORT})
    on_url_match $input "/test" test_handler
done
