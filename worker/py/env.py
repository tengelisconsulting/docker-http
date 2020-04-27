import os
from typing import NamedTuple


class _ENV(NamedTuple):
    WORK_PORT = os.environ["WORK_PORT"]
ENV = _ENV()
