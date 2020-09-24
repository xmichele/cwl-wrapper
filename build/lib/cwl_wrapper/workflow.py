from yaml import load

class Workflow:

    def __init__(self, args):
        self.args = args
        print(self.args)


# https://github.com/common-workflow-language/cwl2argparse/tree/main/cwl2argparse