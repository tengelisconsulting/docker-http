import os
from typing import NamedTuple


class _ENV(NamedTuple):
    SERVICES = os.environ["SERVICES"]
    WORK_PORT = os.environ["WORK_PORT"]
ENV = _ENV()
