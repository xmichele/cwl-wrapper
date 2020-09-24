import argparse
import sys
import os


def arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="cwl-wrapper."
    )

    parser.add_argument('cwlFie', metavar='user_file', type=str, help='user cwl')

    parser.add_argument(
        "--outdir",
        type=str,
        default=os.path.abspath("."),
        help="Output directory, default current directory",
    )

    parser.add_argument(
        "--mainwf",
        type=str,
        default="mainwf.yaml",
        help="main workflow path template path. default=mainwf.yaml",
    )

    parser.add_argument(
        "--stageout",
        type=str,
        default="stagein.yaml",
        help="stageout template path. default=stagein.yaml",
    )

    parser.add_argument(
        "--stagein",
        type=str,
        default="stageout.yaml",
        help="stageout  template path. default=stageout.yaml",
    )

    return parser
