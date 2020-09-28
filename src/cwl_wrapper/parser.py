from yaml import full_load as load_yaml_file
from .rulez import Rulez
from .workflow import Workflow


class Parser:
    rulez = None
    workflow = None

    def __init__(self, kwargs):

        self.rulez = Rulez(kwargs["rulez"])

        self.workflow = Workflow(kwargs,self.rulez)

        inputs = self.workflow.get_inputs()
        if inputs is not None:
            for input in inputs:
                ccc= inputs[input]
                print(ccc.id ,ccc.type)
                # print("req:",str(ccc.get_type()) )
                print(ccc.items , "\n")
                pass

        print ("---------")
        inputs = self.workflow.get_outputs()
        if inputs is not None:
            for input in inputs:
                ccc= inputs[input]
                print(ccc.id ,ccc.type)
                # print("req:",str(ccc.get_type()) )
                print(ccc.items , "\n")
                pass



        # print(str(self.workflow))
