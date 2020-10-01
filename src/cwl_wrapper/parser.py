from yaml import full_load as load_yaml_file
# from yaml import dump as write_yaml_file
from yaml import safe_dump as write_yaml_file

from .rulez import Rulez
from .workflow import Workflow
from .blender import Blender


class Parser:
    rulez = None
    workflow = None

    def __init__(self, kwargs):
        # print(str(kwargs))
        self.rulez = Rulez(kwargs["rulez"])
        self.blender = Blender(kwargs, self.rulez)
        self.workflow = Workflow(kwargs, self.rulez)

        if self.rulez.get('/parser/driver') == "cwl":
            with open(kwargs["maincwl"]) as f:
                self.blender.set_main_workflow(load_yaml_file(f))

            with open(kwargs["stagein"]) as f:
                self.blender.set_stage_in(load_yaml_file(f))

            with open(kwargs["stageout"]) as f:
                self.blender.set_stage_out(load_yaml_file(f))

        self.blender.set_user_workflow(self.workflow)
        out = self.blender.get_output()

        if self.rulez.get('/output/driver') == "cwl":
            with open(self.rulez.get('output/name'), 'w+') as ff:
                write_yaml_file(out, ff, allow_unicode=True)

        # inputs = self.workflow.get_raw_inputs()
        # outputs = self.workflow.get_raw_outputs()
