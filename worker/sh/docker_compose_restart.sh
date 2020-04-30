#!/bin/sh

DC_FILE="${1}"
ENV_FILE="${2}"


. ${ENV_FILE} \
    && docker-compose -f ${DC_FILE} pull \
    && docker-compose -f ${DC_FILE} down \
    && docker-compose -f ${DC_FILE} up -d
