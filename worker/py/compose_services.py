import logging
import subprocess
from typing import Tuple


COMPOSE_DIR = "/srv/compose_configs"


def get_compose_services()-> Tuple[str, ...]:
    configs = subprocess.check_output([
        "ls", COMPOSE_DIR
    ]) \
                        .decode("utf-8") \
                        .split()
    relevant = tuple(
        configs
        # service for service in configs if service != "example"
    )
    logging.info("loaded compose configs: %s", relevant)
    return relevant


def restart_compose_service(service_name: str)-> None:
    subprocess.run([
        "docker_compose_restart.sh",
        f"{COMPOSE_DIR}/{service_name}/docker-compose.yaml",
        f"{COMPOSE_DIR}/{service_name}/env"
    ])
