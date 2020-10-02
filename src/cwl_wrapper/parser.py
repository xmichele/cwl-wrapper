from yaml import full_load as load_yaml_file
from yaml import safe_dump as write_yaml_file

from .rulez import Rulez
from .workflow import Workflow
from .blender import Blender
from .cwl.t2cwl import CWLParserTool

import sys


class Parser:
    rulez = None
    workflow = None
    out = None

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

        else:
            raise Exception('Driver parser: ' + self.rulez.get('/parser/driver') + ' not found')

        self.blender.set_user_workflow(self.workflow)
        self.out = self.blender.get_output()

        if type(self.out) is dict:
            if self.rulez.get('/output/type') == '$graph':
                if self.rulez.get('/output/driver') == "cwl":
                    self.out = {'$graph': [self.out]}

                    psa = CWLParserTool(kwargs["cwl"])

                    if psa.is_graph():
                        graph_res = psa.get_graph_classes()
                        for it in graph_res:
                            self.out['$graph'].append(it)

                        non_graph_res = psa.get_non_graph()
                        for it in non_graph_res:
                            if type(it) is str:
                                self.out[it] = non_graph_res[it]
                    else:
                        raise Exception('Cwl $graph type can\'t be parser')
                else:
                    raise Exception('Driver output: ' + self.rulez.get('/output/driver') + ' not found')
            else:
                raise Exception('Driver output: ' + self.rulez.get('/output/type') + ' not found')

    def write_output(self):
        if self.rulez.get('/output/driver') == "cwl":
            # write_yaml_file(self.out, sys.stdout, allow_unicode=True)
            with open(self.rulez.get('output/name'), 'w+') as ff:
                write_yaml_file(self.out, ff, allow_unicode=True)

    def get_output(self):
        if self.rulez.get('/output/driver') == "cwl":
            write_yaml_file(self.out, sys.stdout, allow_unicode=True)
            # with open(self.rulez.get('output/name'), 'w+') as ff:
            #     write_yaml_file(self.out, ff, allow_unicode=True)
