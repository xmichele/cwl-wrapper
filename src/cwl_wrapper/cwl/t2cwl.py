import sys

from yaml import full_load
from collections import OrderedDict


class InputBinding:
    def __init__(self, ib):
        self.position = ib.get('position', None)
        self.prefix = ib.get('prefix', None)


class OutputBinding:
    def __init__(self, ob):
        self.glob = ob.get('glob', None)


class Param:
    optional = False
    default = None
    type = None
    items = None

    def get_type(self):
        return self.type


class InputParam(Param):
    def __init__(self, param):
        if 'id' not in param:
            raise Exception('Input without id')
        else:
            self.id = param['id']

        self.type = param.get('type', None)
        self.items = []
        if type(self.type) is str and self.type[-2:] == '[]':
            self.items = []
            self.items.append(self.type[:-2])
            self.type = "array"
        if type(self.type) is list and self.type[0] == 'null':
            self.optional = True
        elif type(self.type) is str and self.type[-1] == '?':
            self.optional = True
            self.type = self.type[:-1]
        else:
            self.optional = False

        if type(self.type) is dict:
            if 'type' in self.type and 'items' in self.type:
                if self.type['type'] == 'array':
                    self.items = self.type['items']
                    self.type = 'array'

        self.description = param.get('doc', param.get('description', None))
        self.default = param.get('default', None)
        input_binding = param.get('inputBinding', None)
        if input_binding:
            self.input_binding = InputBinding(input_binding)
        self.stac_catalog = param.get('stac:catalog', None)

        if type(self.items) == str:
            s = self.items
            self.items = []
            self.items.append(s)


class Workflow:
    outputs = None
    inputs = None

    @classmethod
    def graph_parser(self, cwl):
        graph = cwl['$graph']
        for it in graph:
            if 'class' in it:
                if it['class'] == "Workflow":
                    return it

        return None

    def __init__(self, file_cwl):

        raw_workflow = None
        with open(file_cwl) as f:
            raw_workflow = full_load(f)

        if '$graph' in raw_workflow:
            jworkflow = self.graph_parser(raw_workflow)
            if jworkflow is None:
                raise ValueError('Wrong Workflow')
        else:
            jworkflow = raw_workflow

        try:
            self.tool_class = jworkflow['class']
        except KeyError:
            sys.exit('`class` attribute of the CWL document not found')
        if self.tool_class != 'Workflow':
            raise ValueError('Wrong Workflow class')

        self.inputs = OrderedDict()

        if type(jworkflow['inputs']) is list:  # ids not mapped
            for param_dict in jworkflow['inputs']:
                param = InputParam(param_dict)
                self.inputs[param.id] = param
        elif type(jworkflow['inputs']) is dict:  # ids mapped
            for id, param_dict in jworkflow['inputs'].items():
                param_dict['id'] = id
                param = InputParam(param_dict)
                self.inputs[id] = param

        self.outputs = OrderedDict()
        if jworkflow['outputs']:
            if type(jworkflow['outputs']) is list:  # ids not mapped
                for param_dict in jworkflow['outputs']:
                    param = InputParam(param_dict)
                    self.outputs[param.id] = param
            elif type(jworkflow['outputs']) is dict:  # ids mapped
                for id, param_dict in jworkflow['outputs'].items():
                    param_dict['id'] = id
                    param = InputParam(param_dict)
                    self.outputs[id] = param
        self.description = jworkflow.get('doc', jworkflow.get('description', None))
        self.cwl_version = jworkflow.get('cwlVersion', '')
        self.id = jworkflow.get('id', '')
        if 'inputs' in jworkflow:
            self.raw_all_inputs = jworkflow['inputs']
        else:
            self.raw_all_inputs = {}

    def get_inputs(self):
        return self.inputs

    def get_outputs(self):
        return self.outputs
