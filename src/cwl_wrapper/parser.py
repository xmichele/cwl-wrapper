from yaml import full_load as load_yaml_file
from .rulez import Rulez
from .workflow import Workflow


class Parser:
    rulez = None
    workflow = None

    def __init__(self, kwargs):

        self.rulez = Rulez(kwargs["rulez"])

        self.workflow = Workflow(kwargs,self.rulez)

        # inputs = self.workflow.get_raw_inputs()
        # outputs = self.workflow.get_raw_outputs()

        inputs = self.workflow.get_inputs_directory()
        for i in inputs:
            print(i)



