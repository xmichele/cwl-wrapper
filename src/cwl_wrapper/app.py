import logging
import os
import sys
import click
from typing import (
    Any,
    List,
    Optional
)



from .parser import Parser
@click.command()
@click.option('--output', 
              'output', 
              default='-', 
              help='default main cel template maincwl.yaml')
@click.option('--stagein', 
              'stagein', 
              default=None,
              help='default stagein template stagein.yaml')
@click.option('--stageout', 
              'stageout',
              default=None,
              help='default "stageout" template stageout.yaml')
@click.option('--maincwl', 
              'maincwl', 
              default=None,
              help='.... maincwl.yaml')
@click.option('--rulez', 
              'rulez', 
              default=None,
              help='.... rules.yaml')
@click.argument('cwl')
def main(**kwargs):
    """
    The cwl-parser
    """
    wf = Parser(kwargs)
    wf.write_output()


if __name__ == '__main__':
    main()
