import typing
from typing import Dict

from cwl_wrapper.cwl.t2cwl import InputParam
from loguru import logger

from .cwl.t2cwl import Workflow as CWLWorkflow
from .rulez import Rulez


class Directory:
    is_array = False
    is_optional = False
    id: str = None

    def __init__(self, id: str, is_array, is_optional=False, raw=None):
        self.id = id
        self.is_array = is_array
        self.is_optional = is_optional
        self.raw = raw

    def __str__(self):
        return str({"id": self.id, "is_array": self.is_array, "is_optional": self.is_optional})


def parse_cwl_param_directory(input_params: Dict[str, InputParam]) -> typing.List[Directory]:
    res = []
    for key, input_param in input_params.items():

        logger.info(f"{key} - {input_param.type}")

        if input_param.type in ["Directory"]:
            res.append(
                Directory(
                    id=input_param.id, is_array=False, is_optional=input_param.optional, raw=input_param
                )
            )

        elif input_param.type == "array":
            for it in input_param.items:
                if type(it) == str and it in ["Directory"]:
                    res.append(
                        Directory(
                            id=input_param.id,
                            is_array=True,
                            is_optional=input_param.optional,
                            raw=input_param,
                        )
                    )
                    break

    return res


class Workflow:
    wf = None
    driver = None

    def __init__(self, cwl, rulez: Rulez, workflow_id: str = None):
        # print(args)
        if rulez.get("/parser/driver") == "cwl":
            self.wf = CWLWorkflow(cwl, workflow_id)
            self.driver = "cwl"
        else:
            raise ValueError("Rules driver not found or unknown")

    def get_raw_all_inputs(self):
        return self.wf.raw_all_inputs

    def get_raw_all_outputs(self):
        return self.wf.raw_all_outputs

    def get_raw_inputs(self):
        return self.wf.get_inputs()

    def get_raw_outputs(self):
        return self.wf.get_outputs()

    def get_inputs_directory(self):
        if self.driver == "cwl":
            return parse_cwl_param_directory(self.get_raw_inputs())

    def get_outputs_directory(self):
        if self.driver == "cwl":
            return parse_cwl_param_directory(self.get_raw_outputs())

    def get_raw_workflow(self):
        return self.wf.get_raw_workflow()

    def get_id(self):
        if self.driver == "cwl":
            return self.wf.id

        return ""

    def __str__(self):
        return "workflow"  # "#self.wf['id']


class CWL:
    pass
