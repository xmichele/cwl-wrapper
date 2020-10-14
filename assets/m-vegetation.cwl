$graph:
- class: Workflow
  doc: Main stage manager
  id: stage-manager
  inputs:
    aoi:
      doc: Area of interest in WKT
      id: aoi
      label: Area of interest
      type: string
    input_reference:
      doc: EO product for vegetation index
      id: input_reference
      label: EO product for vegetation index
      type: string[]
    job:
      doc: ''
      label: ''
      type: string
    outputfile:
      doc: ''
      label: ''
      type: string
    store_apikey:
      doc: ''
      label: ''
      type: string
    store_host:
      doc: ''
      label: ''
      type: string
    store_username:
      doc: ''
      label: ''
      type: string
  label: theStage
  outputs:
    wf_outputs:
      outputSource:
      - node_stage_out/wf_outputs_out
      type:
        items: Directory
        type: array
  requirements:
    ScatterFeatureRequirement: {}
    SubworkflowFeatureRequirement: {}
  steps:
    node_stage_in:
      in:
        input_reference: input_reference
      out:
      - input_reference_out
      run:
        arguments:
        - position: 1
          prefix: -t
          valueFrom: ./
        baseCommand: stage-in
        class: CommandLineTool
        hints:
          DockerRequirement:
            dockerPull: eoepca/stage-in:0.2
        id: stagein
        inputs:
          input_reference:
            inputBinding:
              position: 2
            type: string
        outputs:
          input_reference_out:
            outputBinding:
              glob: .
            type: Directory
        requirements:
          EnvVarRequirement:
            envDef:
              PATH: /opt/anaconda/envs/env_stagein/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
          ResourceRequirement: {}
      scatter: input_reference
      scatterMethod: dotproduct
    node_stage_out:
      in:
        job: job
        outputfile: outputfile
        store_apikey: store_apikey
        store_host: store_host
        store_username: store_username
        wf_outputs: on_stage/wf_outputs
      out:
      - wf_outputs_out
      run:
        baseCommand: stage-out
        class: CommandLineTool
        hints:
          DockerRequirement:
            dockerPull: eoepca/stage-out:0.2
        inputs:
          job:
            inputBinding:
              position: 1
              prefix: --job
            type: string
          outputfile:
            inputBinding:
              position: 5
              prefix: --outputfile
            type: string
          store_apikey:
            inputBinding:
              position: 4
              prefix: --store-apikey
            type: string
          store_host:
            inputBinding:
              position: 2
              prefix: --store-host
            type: string
          store_username:
            inputBinding:
              position: 3
              prefix: --store-username
            type: string
          wf_outputs:
            inputBinding:
              position: 6
            type: Directory[]
        outputs:
          wf_outputs_out:
            outputBinding:
              glob: .
            type: Directory[]
        requirements:
          EnvVarRequirement:
            envDef:
              PATH: /opt/anaconda/envs/env_stageout/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
          ResourceRequirement: {}
    on_stage:
      in:
        aoi: aoi
        input_reference: node_stage_in/input_reference_out
      out:
      - wf_outputs
      run: '#vegetation-index'
- baseCommand: vegetation-index
  class: CommandLineTool
  hints:
    DockerRequirement:
      dockerPull: eoepca/vegetation-index:0.2
  id: clt
  inputs:
    inp1:
      inputBinding:
        position: 1
        prefix: --input_reference
      type: Directory
    inp2:
      inputBinding:
        position: 2
        prefix: --aoi
      type: string
  outputs:
    results:
      outputBinding:
        glob: .
      type: Directory
  requirements:
    EnvVarRequirement:
      envDef:
        PATH: /opt/anaconda/envs/env_vi/bin:/opt/anaconda/envs/env_vi/bin:/home/fbrito/.nvm/versions/node/v10.21.0/bin:/opt/anaconda/envs/notebook/bin:/opt/anaconda/bin:/usr/share/java/maven/bin:/opt/anaconda/bin:/opt/anaconda/envs/notebook/bin:/opt/anaconda/bin:/usr/share/java/maven/bin:/opt/anaconda/bin:/opt/anaconda/condabin:/opt/anaconda/envs/notebook/bin:/opt/anaconda/bin:/usr/lib64/qt-3.3/bin:/usr/share/java/maven/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/fbrito/.local/bin:/home/fbrito/bin:/home/fbrito/.local/bin:/home/fbrito/bin
        PREFIX: /opt/anaconda/envs/env_vi
    ResourceRequirement: {}
  stderr: std.err
  stdout: std.out
- class: Workflow
  doc: Vegetation index processor, the greatest
  id: vegetation-index
  inputs:
    aoi:
      doc: Area of interest in WKT
      label: Area of interest
      type: string
    input_reference:
      doc: EO product for vegetation index
      label: EO product for vegetation index
      type: Directory[]
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
cwlVersion: v1.0
