from typing import Tuple

from apptypes import App
import services


def restart_service(
        app: App,
        frames: Tuple[bytes]
)-> None:
    service_name = frames[0].decode("utf-8")
    assert service_name in app.services
    services.restart_service(app.services[service_name])
    return


HANDLER_MAP = {
    b"restart_service": restart_service,
}
