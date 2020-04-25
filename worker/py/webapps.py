import logging
import re
import subprocess
from typing import Dict

from env import ENV

SERVICE_CONF_REGEX = re.compile("(\w*)=(\d+),(\d+)")


def _derive_conf()-> Dict:
    res = {}
    services = ENV.SERVICES.split(";")
    for service in services:
        name, port_1, port_2 = re.match(SERVICE_CONF_REGEX, service) \
                                .groups()
        res[name] = [port_1, port_2] # could be dynamic number
    return res
WEBAPP_CONF = _derive_conf()


def restart_webapp_service(
        image_name: str,
        container_name: str,
        vsn: str,
        ports: [int, int]
)-> None:
    subprocess.run([
        "docker", "run", "-d", "--net=host", "--rm",
        "-e", f"PORT={ports[0]}",
        "--name", container_name,
        f"{image_name}:{vsn}"
    ])
