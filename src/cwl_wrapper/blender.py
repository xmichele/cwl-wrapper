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
            step[name]['out'] = {}

        if 'in' not in step[name]:
            step[name]['in'] = {}

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
                print(str(it))
                self.__prepare_step_run(steps, start_node_name)

                the_command = self.main_stage_in
                the_command_imputs = the_command['inputs']
                the_val = self.rulez.get('/cwl/Directory[]') if it.is_array else self.rulez.get('/cwl/Directory')

                if type(the_command_imputs) is list:
                    the_val['id'] = it.id
                    the_command_imputs.append(the_val)
                elif type(the_command_imputs) is dict:
                    the_command_imputs[it.id] = the_val

                steps[start_node_name]['in'][it.id] = it.id
                steps[start_node_name]['run'] = the_command

                cursor = cursor + 1
                start_node_name = connection_node_node_stage_in + '_' + str(cursor)

    def set_main_workflow(self, wf_main):
        self.main_wf = wf_main

    def set_stage_in(self, wf_in):
        self.main_stage_in = wf_in
        if 'inputs' not in self.main_stage_in:
            self.main_stage_in['inputs'] = {}

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
