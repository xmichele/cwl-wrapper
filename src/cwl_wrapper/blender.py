from .rulez import Rulez
from .workflow import Workflow


class Blender:
    def __init__(self, kwargs, rulez: Rulez):
        self.rulez = rulez
        self.main_wf = None
        self.main_stage_in = None
        self.main_stage_out = None

        self.inputs = []
        self.outputs = []

    def __add_stage_in_cwl(self):
        driver = self.rulez.get('/onstage/driver')
        connection_node_node_stage_in = self.rulez.get('/onstage/stage_in/connection_node')
        if connection_node_node_stage_in == '':
            connection_node_node_stage_in = 'node_stage_in'

        if self.main_wf is None:
            raise Exception('maincwl.yaml not defined')

        start_step = None
        if 'steps' not in self.main_wf:
            start_step = {
                connection_node_node_stage_in: {
                    'in': [],
                    'out': [],
                    'run': ''},
            }
            self.main_wf['steps'] = start_step
        else:
            if connection_node_node_stage_in in self.main_wf['steps']:
                # steps exist
                start_step = self.main_wf['steps'][connection_node_node_stage_in]
            else:
                raise Exception("Cant't find entry point: " + connection_node_node_stage_in)



        print(start_step)



        # self.main_wf['steps'][node]['run'] = self.main_stage_in
        #
        # # check if is required ScatterFeature
        # if len(self.inputs) > 0:
        #     for it in self.inputs:
        #         print(it)

        pass

    def set_main_workflow(self, wf_main):
        self.main_wf = wf_main
        pass

    def set_stagein(self, wf_in):
        self.main_stage_in = wf_in
        pass

    def set_stageout(self, wf_out):
        pass

    def set_inputs(self, inputs):
        self.inputs = inputs

    def set_outputs(self, outputs):
        self.outputs = outputs

    def get_output(self):

        if self.rulez.get('/onstage/driver') == 'cwl':
            self.__add_stage_in_cwl()
        else:
            raise Exception('Driver onstage: ' + self.rulez.get('/output/driver') + ' not found')

        if self.rulez.get('/output/type') == '$graph':
            return {'$graph': self.main_wf}
        else:
            raise Exception('Driver output: ' + self.rulez.get('/output/type') + ' not found')
