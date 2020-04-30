import logging
import os
from types import SimpleNamespace
from typing import Dict

import yaml
import zmq
import zmq.asyncio

from apptypes import App
from compose_services import get_compose_services
from env import ENV
from services import load_service_conf


def reconnect(app: App)-> App:
    if app.work_endpoint:
        app.work_endpoint.setsockopt(zmq.LINGER, 0)
        app.work_endpoint.close()
    logging.info("connected to %s", app.work_addr)
    app.work_endpoint = app.ctx.socket(zmq.ROUTER)
    app.work_endpoint.bind(app.work_addr)
    return app


def init()-> App:
    app = App(
        compose_services = get_compose_services(),
        ctx = zmq.asyncio.Context(),
        # con_timeout_s = 0,
        services = load_service_conf(),
        work_endpoint = None,
        work_addr = f"tcp://*:{ENV.WORK_PORT}",
    )
    app = reconnect(app)
    return app
