from .utils import looking_for
from .cwl.t2cwl import Workflow as CWLWorkflow
from .rulez import Rulez


class Workflow:
    wf = None

    def __init__(self, args, rulez: Rulez):
        # print(args)
        if rulez.driver == 'cwl':
            self.wf = CWLWorkflow(args['cwl'])
        else:
            raise ValueError('rules driver.....')

    def get_inputs(self):
        return self.wf.get_inputs()

    def get_outputs(self):
        return self.wf.get_outputs()

    def __str__(self):
        return 'workflow'  # "#self.wf['id']
