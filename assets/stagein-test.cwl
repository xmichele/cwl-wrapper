baseCommand: stage-in
class: CommandLineTool
hints:
  DockerRequirement:
    dockerPull: eoepca/stage-in:0.2
id: stagein
arguments:
  - prefix: -t
    position: 1
    valueFrom: "./"

inputs:
    parameter_A:
      doc: EO product for vegetation index
      label: EO product for vegetation index
      type: string[]
    parameter_B:
      doc: EO product for vegetation index
      label: EO product for vegetation index
      type: string[]
outputs: {}
requirements:
  EnvVarRequirement:
    envDef:
      PATH: /opt/anaconda/envs/env_stagein/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
  ResourceRequirement: {}