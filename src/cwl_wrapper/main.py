import logging
import os
import signal
import sys
from typing import (
    Any,
    List,
    Optional
)
from .arguments import arg_parser as arp
from .workflow import Workflow


def _terminate_processes() -> None:
    pass


def _signal_handler(signum: int, _: Any) -> None:
    _terminate_processes()
    sys.exit(signum)


def main(
        args: Optional[List[str]] = None, **kwargs):
    allA = arp().parse_args(args)
    wf = Workflow(allA)


def run(*args, **kwargs):
    signal.signal(signal.SIGTERM, _signal_handler)
    main(*args, **kwargs)
