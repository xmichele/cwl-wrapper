
import argparse
import sys
import os

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

def arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="cwl-wrapper."
    )

    parser.add_argument('cwlFie', metavar='user_file', type=str ,help='user cwl')

    parser.add_argument(
        "--outdir",
        type=str,
        default=os.path.abspath("."),
        help="Output directory, default current directory",
    )

    parser.add_argument(
        "--stageout",
        type=str,
        default="stagein.cwl",
        help="stageout template path. default=stagein.cwl",
    )

    parser.add_argument(
        "--stagein",
        type=str,
        default="stageout.cwl",
        help="stageout  template path. default=stageout.cwl",
    )

    return parser
