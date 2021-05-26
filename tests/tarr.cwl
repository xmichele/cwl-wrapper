$graph:
- baseCommand: test1.py
  class: CommandLineTool
  id: clt
  inputs:
    input_reference:
      type:
        inputBinding:
          position: 1
          prefix: --input_reference
        items: Directory
        type: array
    input_reference_opt:
      inputBinding:
        position: 2
        prefix: --input_reference_opt
      type:
      - 'null'
      - items: Directory
        type: array
    aoi:
      inputBinding:
        position: 3
        prefix: --aoi
      type: string?
    conf_file:
      inputBinding:
        position: 4
        prefix: --file
      type: File?
    mode:
      inputBinding:
        position: 5
        prefix: --mode
      type:
      - 'null'
      - symbols: &id001
        - local
        - ftp
        type: enum
  outputs:
    results:
      outputBinding:
        glob: .
      type: Directory
  requirements:
    EnvVarRequirement:
      envDef:
        PATH: /srv/conda/envs/env_cwl_wrapper/bin:/srv/conda/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
    ResourceRequirement: {}
  stderr: std.err
  stdout: std.out
- class: Workflow
  doc: hello Im the doc of Workflow class
  id: test1.py
  inputs:
    input_reference:
      doc: this input reference
      label: this input reference
      type: Directory[]
    input_reference_opt:
      doc: this input reference
      label: this input reference
      type: Directory[]?
    aoi:
      doc: help for the area of interest
      label: help for the area of interest
      type: string?
    conf_file:
      doc: help for the conf file
      label: help for the conf file
      type: File?
    mode:
      doc: null
      label: null
      type:
      - 'null'
      - symbols: *id001
        type: enum
  label: hello Im the label of Workflow class
  outputs:
  - id: wf_outputs
    outputSource:
    - step_1/results
    type: Directory
  steps:
    step_1:
      in:
        input_reference: input_reference
        input_reference_opt: input_reference_opt
        aoi: aoi
        conf_file: conf_file
        mode: mode
      out:
      - results
      run: '#clt'
$namespaces:
  s: https://schema.org/
cwlVersion: v1.0
schemas:
- http://schema.org/version/9.0/schemaorg-current-http.rdf

