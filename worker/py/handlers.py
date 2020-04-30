import logging
from typing import Callable
from typing import Dict
from typing import Tuple

from apptypes import App
import compose_services
import services


def restart_service(
        app: App,
        frames: Tuple[bytes, ...]
)-> None:
    service_name = frames[0].decode("utf-8")
    assert service_name in app.services
    conf = app.services[service_name]
    services.ensure_latest(conf)
    services.restart_service(conf)
    return


def restart_compose_service(
        app: App,
        frames: Tuple[bytes, ...]
)-> None:
    service_name = frames[0].decode("utf-8")
    assert service_name in app.compose_services
    compose_services.restart_compose_service(service_name)


HANDLER_MAP: Dict[
    bytes,
    Callable[[App, Tuple[bytes, ...]],
             None]
] = {
    b"restart_compose_service": restart_compose_service,
    b"restart_service": restart_service,
}
