import logging
import os
import signal
import sys
from typing import (
    IO,
    Any,
    Callable,
    Dict,
    List,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sized,
    TextIO,
    Tuple,
    Union,
    cast,
)
from .arguments import arg_parser as arp

def _terminate_processes() -> None:
    pass


def _signal_handler(signum: int, _: Any) -> None:
    _terminate_processes()
    sys.exit(signum)


def main(
        args: Optional[List[str]] = None, **kwargs):
    a = arp().parse_args(args)

    print(a.cwlFie)


def run(*args, **kwargs):
    signal.signal(signal.SIGTERM, _signal_handler)
    main(*args, **kwargs)
