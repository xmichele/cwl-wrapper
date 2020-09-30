from yaml import full_load as load_yaml_file
from .rulez import Rulez
from .workflow import Workflow
from .blender import Blender

class Parser:
    rulez = None
    workflow = None

    def __init__(self, kwargs):
        print(str(kwargs))
        self.rulez = Rulez(kwargs["rulez"])
        self.blender = Blender(kwargs,self.rulez)

        load_driver = self.rulez.parser_driver
        if load_driver == "cwl":
            with open(kwargs["maincwl"]) as f:
                self.blender.set_main_workflow(load_yaml_file(f))

            with open(kwargs["stagein"]) as f:
                self.blender.set_stagein(load_yaml_file(f))

            with open(kwargs["stageout"]) as f:
                self.blender.set_stageout(load_yaml_file(f))





        self.workflow = Workflow(kwargs,self.rulez)
        # inputs = self.workflow.get_raw_inputs()
        # outputs = self.workflow.get_raw_outputs()

        inputs = self.workflow.get_inputs_directory()
        for i in inputs:
            print(i)



