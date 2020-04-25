#!/bin/sh

echo "WORKING!!!"

curl 127.0.0.1:8888

docker run --net=host -d nginx:1.17-alpine

# IMAGE_VSN="staging-latest"

# IMAGE_NAME="galleri/webapp"
# CONTAINER_PREFIX="galleri_port_"

# stop() {
#     PORT="${1}"
#     docker stop ${CONTAINER_PREFIX}${PORT}
# }

# start() {
#     PORT="${1}"
#     docker run -d \
#            --rm \
#            --net=host \
#            -e PORT=${PORT} \
#            --name ${CONTAINER_PREFIX}${PORT} \
#            ${IMAGE_NAME}:${IMAGE_VSN}
# }

# main(){
#     stop 5003 \
#         && start 5003 \
#         && stop 5004 \
#         && start 5004
# }

# main
