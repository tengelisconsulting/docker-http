from types import SimpleNamespace
from typing import Dict
from typing import List
from typing import NamedTuple
from typing import Tuple

import zmq.asyncio


class WebContainerConf(NamedTuple):
    image_name: str
    container_prefix: str
    tag: str
    ports: List[int]


class App(SimpleNamespace):
    ctx: zmq.asyncio.Context
    compose_services: Tuple[str, ...]
    # con_timeout_s: int
    services: Dict[str, WebContainerConf]
    work_endpoint: zmq.asyncio.Socket
    work_addr: str
