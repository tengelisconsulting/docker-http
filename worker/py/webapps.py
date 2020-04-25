import logging
import re
import subprocess
from typing import Dict
from typing import NamedTuple
from typing import List

from env import ENV

SERVICE_CONF_REGEX = re.compile("(\w*)=(\d+),(\d+)")

class ContainerConf(NamedTuple):
    image_name: str
    container_name: str
    vsn: str
    ports: List[int]


def _derive_conf()-> Dict:
    res = {}
    services = ENV.SERVICES.split(";")
    for service in services:
        name, port_1, port_2 = re.match(SERVICE_CONF_REGEX, service) \
                                .groups()
        res[name] = [port_1, port_2] # could be dynamic number
    return res
WEBAPP_CONF = _derive_conf()


def restart_webapp_service(conf: ContainerConf)-> None:
    for i in range(0, 2):
        stop_webapp_service(conf, i)
        start_webapp_service(conf, i)
    return

def stop_webapp_service(
        conf: ContainerConf,
        instance: int
)-> None:
    port = conf.ports[instance]
    subprocess.run([
        "docker", "stop", f"{conf.container_name}_{port}"
    ])
    return


def start_webapp_service(
        conf: ContainerConf,
        instance: int
)-> None:
    port = conf.ports[instance]
    subprocess.run([
        "docker", "run", "-d", "--net=host", "--rm",
        "-e", f"PORT={port}",
        "--name", f"{conf.container_name}_{port}",
        f"{conf.image_name}:{conf.vsn}"
    ])
    return
