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

    @staticmethod
    def __prepare_step_run(step, name):

        if name not in step:
            step[name] = {}

        if 'run' not in step[name]:
            step[name]['run'] = {}

        if 'out' not in step[name]:
            step[name]['out'] = []

        if 'in' not in step[name]:
            step[name]['in'] = []

    def __add_stage_in_graph_cwl(self, start):
        driver = self.rulez.get('/onstage/driver')
        if len(self.inputs) > 0 and type(start) is list:

            connection_node_node_stage_in = self.rulez.get('/onstage/stage_in/connection_node')
            if connection_node_node_stage_in == '':
                connection_node_node_stage_in = 'node_stage_in'

            if self.main_wf is None:
                raise Exception('maincwl.yaml not defined')

            if 'steps' not in self.main_wf:
                # steps does not exist
                self.main_wf['steps'] = {}

            steps = self.main_wf['steps']
            cursor = 0
            start_node_name = connection_node_node_stage_in
            for it in self.inputs:
                if not it.is_array:
                    print(str(it))
                    self.__prepare_step_run(steps, start_node_name)

                    steps[start_node_name]['run'] = self.main_stage_in

                    cursor = cursor + 1
                    start_node_name = connection_node_node_stage_in + '_' + str(cursor)

    def set_main_workflow(self, wf_main):
        self.main_wf = wf_main

    def set_stage_in(self, wf_in):
        self.main_stage_in = wf_in

    def set_stage_out(self, wf_out):
        pass

    def set_inputs(self, inputs):
        self.inputs = inputs

    def set_outputs(self, outputs):
        self.outputs = outputs

    def get_output(self):

        start = self.main_wf
        if self.rulez.get('/output/type') == '$graph':
            start = {'$graph': [self.main_wf]}
        else:
            raise Exception('Driver output: ' + self.rulez.get('/output/type') + ' not found')

        if self.rulez.get('/onstage/driver') == 'cwl':
            if self.rulez.get('/output/type') == '$graph':
                self.__add_stage_in_graph_cwl(start['$graph'])
            else:
                raise Exception("Non $graph request")
        else:
            raise Exception('Driver onstage: ' + self.rulez.get('/output/driver') + ' not found')

        return start
