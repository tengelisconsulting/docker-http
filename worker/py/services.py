import logging
import re
import subprocess
from typing import Dict

import yaml

from apptypes import ContainerConf
from env import ENV


def load_service_conf()-> Dict[str, ContainerConf]:
    with open("/srv/conf/conf.yaml") as conf_f:
        all_conf = yaml.safe_load(conf_f)
        all_service_conf = all_conf["services"]
        conf = {}
        for service_name in all_service_conf:
            service_conf = all_service_conf[service_name]
            conf[service_name] = ContainerConf(
                image_name = service_conf["image"],
                container_prefix = service_name,
                tag = service_conf["tag"],
                ports = service_conf["ports"]
            )
        return conf


def restart_service(conf: ContainerConf)-> None:
    for i in range(0, len(conf.ports)):
        stop_service(conf, i)
        start_service(conf, i)


def start_service(
        conf: ContainerConf,
        instance: int
)-> None:
    port = conf.ports[instance]
    subprocess.run([
        "docker", "run", "-d", "--net=host", "--rm",
        "-e", f"PORT={port}",
        "--name", f"{conf.container_prefix}_{port}",
        f"{conf.image_name}:{conf.tag}"
    ])
    return


def stop_service(
        conf: ContainerConf,
        instance: int
)-> None:
    port = conf.ports[instance]
    subprocess.run([
        "docker", "stop", f"{conf.container_prefix}_{port}"
    ])
    return
