#!/usr/bin/env bash



while true; do
    input=$(nc -l -p ${LOCAL_HOOK_PORT})
    echo "input"
    echo ${input}
done
