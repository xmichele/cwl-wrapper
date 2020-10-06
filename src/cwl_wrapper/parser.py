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
    output_name = '-'

    def __init__(self, kwargs):
        # print(str(kwargs))
        self.rulez = Rulez(kwargs["rulez"])
        self.blender = Blender(kwargs, self.rulez)
        self.workflow = Workflow(kwargs, self.rulez)
        self.output_name = kwargs['output']

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
                        the_graph = self.out['$graph']
                        for it in graph_res:
                            the_graph.append(it)

                        non_graph_res = psa.get_non_graph()
                        for it in non_graph_res:
                            if type(it) is dict:
                                for i in it:
                                    self.out[i] = it[i]
                    else:
                        raise Exception('Cwl $graph type can\'t be parser')
                else:
                    raise Exception('Driver output: ' + self.rulez.get('/output/driver') + ' not found')
            else:
                raise Exception('Driver output: ' + self.rulez.get('/output/type') + ' not found')

    def write_output(self):
        if self.rulez.get('/output/driver') == "cwl":
            # self.output_name = self.rulez.get('output/name')
            if self.output_name == '-':
                write_yaml_file(self.out, sys.stdout, allow_unicode=True)
                pass
            else:
                with open(self.output_name, 'w+') as ff:
                    write_yaml_file(self.out, ff, allow_unicode=True)

    # def get_output(self):
    #     if self.rulez.get('/output/driver') == "cwl":
    #         write_yaml_file(self.out, sys.stdout, allow_unicode=True)
    #         # with open(self.rulez.get('output/name'), 'w+') as ff:
    #         #     write_yaml_file(self.out, ff, allow_unicode=True)
