import click
from cwl_wrapper.parser import Parser


@click.command()
@click.option("--output", "output", default="-", help="default main cel template assets/maincwl.yaml")
@click.option("--stagein", "stagein", default=None, help="default stagein template assets/stagein.yaml")
@click.option(
    "--stageout", "stageout", default=None, help='default "stageout" template assets/stageout.yaml'
)
@click.option("--maincwl", "maincwl", default=None, help="default maincwl assets/maincwl.yaml")
@click.option("--rulez", "rulez", default=None, help="rules default file assets/rules.yaml")
@click.option("--assets", "assets", default=None, help="use <value> as maincwl from assets/<values>")
@click.argument("cwl")
def main(**kwargs):
    """
    The cwl-parser
    """
    wf = Parser(kwargs)
    wf.write_output()


if __name__ == "__main__":
    main()
