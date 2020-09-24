import logging
import os
import signal
import sys
import click
import pkg_resources
from typing import (
    Any,
    List,
    Optional
)


def _terminate_processes() -> None:
    pass


def _signal_handler(signum: int, _: Any) -> None:
    _terminate_processes()
    sys.exit(signum)


@click.command()
@click.option('--stagein',
              'stagein',
              default='stagein.yaml',
              help='.... stagein.yaml')
@click.option('--stageout',
              'stageout',
              default='stageout.yaml',
              help='.... stageout.yaml')
@click.argument('cwl')
def main(stagein, stageout, cwl):
    signal.signal(signal.SIGTERM, _signal_handler)


    # sav_file = setup_idl(pkg_resources.resource_filename(__package__.split('.')[0], 'idl/hasard_flood_mapping.sav'))

    print(__package__)
    # print(pkg_resources.resource_filename(__package__))

    pass


if __name__ == '__main__':
    main()
