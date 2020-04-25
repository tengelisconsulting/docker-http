#!/usr/bin/env python3

import asyncio
import logging
import time
from typing import Tuple

from app import App
from app import init
from handlers import HANDLER_MAP
import os


def setup_logging(identifier="")-> None:
    def get_log_level()-> int:
        env_log_level_map = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "ERROR": logging.ERROR
        }
        env_log_level = os.environ.get("LOG_LEVEL")
        try:
            return env_log_level_map[env_log_level]
        except:
            return logging.INFO
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(
        level=get_log_level(),
        format=f"{identifier} %(asctime)s.%(msecs)03d "
        "%(levelname)s %(module)s - %(funcName)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


async def handle(work: Tuple[str])-> None:
    logging.info("work: %s", work)
    action = work[0]
    if action not in HANDLER_MAP:
        logging.error("unknown action: %s", action)
        return
    HANDLER_MAP[action](work[1:])
    return


async def handle_loop()-> None:
    app = init()
    while True:
        msg = await app.work_endpoint.recv_multipart()
        return_addr, padding, work = None, None, None
        try:
            return_addr = msg[0]
            padding = msg[1]
            assert padding == b""
            work = tuple(msg[2:])
        except Exception as e:
            logging.exception("bad msg: %s - %s", msg, e)
        try:
            await handle(work)
        except Exception as e:
            logging.exception("handler died: %s", e)


def main():
    setup_logging()
    asyncio.run(handle_loop())


if __name__ == "__main__":
    main()
