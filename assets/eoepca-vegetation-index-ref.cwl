$graph:
- baseCommand: vegetation-index-ref
  class: CommandLineTool
  hints:
    DockerRequirement:
      dockerPull: terradue/eoepca-vegetation-index-ref:0.4
  id: clt
  inputs:
    inp1:
      inputBinding:
        position: 1
        prefix: --input_reference
      type: string
    inp2:
      inputBinding:
        position: 2
        prefix: --aoi
      type: string
  outputs:
    results:
      outputBinding:
        glob: .
      type: Any
  requirements:
    EnvVarRequirement:
      envDef:
        PATH: /opt/anaconda/envs/env_vi/bin:/opt/anaconda/envs/env_vi/bin:/opt/anaconda/envs/env_default/bin:/opt/anaconda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
        PREFIX: /opt/anaconda/envs/env_vi
    ResourceRequirement: {}
  stderr: std.err
  stdout: std.out
- class: Workflow
  doc: Vegetation index processor
  id: vegetation-index-ref
  inputs:
    aoi:
      doc: Area of interest in WKT
      label: Area of interest
      type: string
    input_reference:
      doc: STAC item for vegetation index
      label: STAC item for vegetation index
      type: string[]
  label: Vegetation index
  outputs:
  - id: wf_outputs
    outputSource:
    - node_1/results
    type:
      items: Directory
      type: array
  requirements:
  - class: ScatterFeatureRequirement
  steps:
    node_1:
      in:
        inp1: input_reference
        inp2: aoi
      out:
      - results
      run: '#clt'
      scatter: inp1
      scatterMethod: dotproduct
$namespaces:
  stac: http://www.me.net/stac/cwl/extension
cwlVersion: v1.0
