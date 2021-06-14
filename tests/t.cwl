$graph:
- baseCommand: test1.py
  class: CommandLineTool
  id: clt
  inputs:
    input_path:
      inputBinding:
        position: 1
        prefix: --input_path
      type: Directory
    input_path_pan:
      inputBinding:
        position: 2
        prefix: --input_path_pan
      type: Directory?
  outputs:
    results:
      outputBinding:
        glob: .
      type: Directory
  requirements:
    EnvVarRequirement:
      envDef:
        PATH: /srv/conda/envs/notebook/bin:/srv/conda/condabin:/home/jovyan/.local/bin:/home/jovyan/.local/bin:/srv/conda/envs/notebook/bin:/srv/conda/bin:/srv/npm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    ResourceRequirement: {}
  stderr: std.err
  stdout: std.out
- class: Workflow
  doc: This is Workflow class doc
  id: test1.py
  inputs:
    input_path:
      doc: Path of the directory that contains the catalog.json of the calibrated
        input product (MSS + PAN)
      label: Path of the directory that contains the catalog.json of the calibrated
        input product (MSS + PAN)
      type: Directory[]
    input_path_pan:
      doc: Path of the directory that contains the catalog.json of the PAN-calibrated
        input product (if not included in the input_path)
      label: Path of the directory that contains the catalog.json of the PAN-calibrated
        input product (if not included in the input_path)
      type: Directory?
  label: This is Workflow class label
  outputs:
  - id: wf_outputs
    outputSource:
    - step_1/results
    type: Directory
  steps:
    step_1:
      in:
        input_path: input_path
        input_path_pan: input_path_pan
      out:
      - results
      run: '#clt'
$namespaces:
  s: https://schema.org/
cwlVersion: v1.0
schemas:
- http://schema.org/version/9.0/schemaorg-current-http.rdf

