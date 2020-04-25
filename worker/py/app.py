import logging
import os
from types import SimpleNamespace

import zmq
import zmq.asyncio

from env import ENV


class App(SimpleNamespace):
    ctx: zmq.asyncio.Context
    # con_timeout_s: int
    work_endpoint: zmq.asyncio.Socket
    work_addr: str


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
        ctx = zmq.asyncio.Context(),
        con_timeout_s = 0,
        work_endpoint = None,
        work_addr = f"tcp://*:{ENV.WORK_PORT}",
    )
    app = reconnect(app)
    return app
