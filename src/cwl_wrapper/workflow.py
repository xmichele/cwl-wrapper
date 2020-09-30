from .utils import looking_for
from .cwl.t2cwl import Workflow as CWLWorkflow
from .rulez import Rulez


class Directory:
    is_array = False
    id: str = None

    def __init__(self, id: str, is_array=False):
        self.id = id
        self.is_array = is_array

    def __str__(self):
        return str({'id': self.id, 'is_array': self.is_array})


def parse_cwl_param_directory(vals):
    res = []
    for it in vals:
        cwl_param = vals[it]
        if cwl_param.type == "Directory":
            res.append(Directory(cwl_param.id, False))

        elif cwl_param.type == "array":
            for it in cwl_param.items:
                if type(it) == str and it == 'Directory':
                    res.append(Directory(cwl_param.id, True))
                    break

    return res


class Workflow:
    wf = None
    driver = None

    def __init__(self, args, rulez: Rulez):
        # print(args)
        if rulez.parser_driver == 'cwl':
            self.wf = CWLWorkflow(args['cwl'])
            self.driver = 'cwl'
        else:
            raise ValueError('Rules driver not found or unknown')

    def get_raw_inputs(self):
        return self.wf.get_inputs()

    def get_raw_outputs(self):
        return self.wf.get_outputs()

    def get_inputs_directory(self):
        if self.driver == 'cwl':
            return parse_cwl_param_directory(self.get_raw_inputs())

    def get_outputs_directory(self):
        if self.driver == 'cwl':
            return parse_cwl_param_directory(self.get_raw_outputs())

    def __str__(self):
        return 'workflow'  # "#self.wf['id']
