import logging
import os
#import signal
import sys
import click
import pkg_resources
from typing import (
    Any,
    List,
    Optional
)

aaa


from .parser import Parser
    aa
@click.command()
@click.option('--output', 'output', default='-', help='.... maincwl.yaml')
@click.option('--stagein', 'stagein', default=pkg_resources.resource_filename(__package__, "assets/stagein.yaml"),
              help='.... stagein.yaml')
@click.option('--stageout', 'stageout', default=pkg_resources.resource_filename(__package__, "assets/stageout.yaml"),
              help='.... stageout.yaml')
@click.option('--maincwl', 'maincwl', default=pkg_resources.resource_filename(__package__, "/assets/maincwl.yaml"),
              help='.... maincwl.yaml')
@click.option('--rulez', 'rulez', default=pkg_resources.resource_filename(__package__, "/assets/rulez.yaml"),
              help='.... maincwl.yaml')
@click.argument('cwl')
def main(**kwargs):
    #signal.signal(signal.SIGTERM, _signal_handler)
    wf = Parser(kwargs)
    wf.write_output()


if __name__ == '__main__':
    main()
