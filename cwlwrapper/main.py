
import argparse
import logging
import os
import signal
import sys
 
def _terminate_processes() -> None:
	pass

def _signal_handler(signum: int, val) -> None:
    _terminate_processes()
    sys.exit(signum)

def main(args = None, input_required: bool = True):
    print(args)
    print(input_required)


def run(*args, **kwargs):
   signal.signal(signal.SIGTERM, _signal_handler)
   main(*args, **kwargs)
