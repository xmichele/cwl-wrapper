from .rulez import Rulez
from .workflow import Workflow


class Blender:
    def __init__(self, kwargs, rulez: Rulez):
        self.rulez = rulez
        self.main_wf = ''
        self.main_sin = ''
        self.main_sout = ''
        self.inputs = []
        self.outputs = []

    def set_main_workflow(self, wf_main):
        pass

    def set_stagein(self, wf_main):
        pass

    def set_stageout(self, wf_main):
        pass


    def set_inputs(self,inputs):
        pass

    def set_outputs(self,outputs):
        pass
