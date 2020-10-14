$graph:
- class: Workflow
  doc: Main stage manager
  id: stage-manager
  inputs:
    job:
      doc: ''
      label: ''
      type: string
    ndvi_threshold:
      doc: NDVI difference threshold
      id: ndvi_threshold
      label: NDVI difference threshold
      type: string
    ndwi_threshold:
      doc: NDVI difference threshold
      id: ndwi_threshold
      label: NDVI difference threshold
      type: string
    outputfile:
      doc: ''
      label: ''
      type: string
    post_event:
      doc: Sentinel-2 Level-2A pre-event acquisition
      id: post_event
      label: Sentinel-2 Level-2A pre-event
      type: string
    pre_event:
      doc: Sentinel-2 Level-2A pre-event acquisition
      id: pre_event
      label: Sentinel-2 Level-2A pre-event
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
      type: Directory
  requirements:
    ScatterFeatureRequirement: {}
    SubworkflowFeatureRequirement: {}
  steps:
    node_stage_in:
      in:
        pre_event: pre_event
      out:
      - pre_event_out
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
          pre_event:
            inputBinding:
              position: 2
            type: string
        outputs:
          pre_event_out:
            outputBinding:
              glob: .
            type: Directory
        requirements:
          EnvVarRequirement:
            envDef:
              PATH: /opt/anaconda/envs/env_stagein/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
          ResourceRequirement: {}
    node_stage_in_1:
      in:
        post_event: post_event
      out:
      - post_event_out
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
          post_event:
            inputBinding:
              position: 2
            type: string
        outputs:
          post_event_out:
            outputBinding:
              glob: .
            type: Directory
        requirements:
          EnvVarRequirement:
            envDef:
              PATH: /opt/anaconda/envs/env_stagein/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
          ResourceRequirement: {}
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
            type: Directory
        outputs:
          wf_outputs_out:
            outputBinding:
              glob: .
            type: Directory
        requirements:
          EnvVarRequirement:
            envDef:
              PATH: /opt/anaconda/envs/env_stageout/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
          ResourceRequirement: {}
    on_stage:
      in:
        ndvi_threshold: ndvi_threshold
        ndwi_threshold: ndwi_threshold
        post_event: node_stage_in_1/post_event_out
        pre_event: node_stage_in/pre_event_out
      out:
      - wf_outputs
      run: '#burned-area'
- baseCommand: burned-area
  class: CommandLineTool
  hints:
    DockerRequirement:
      dockerPull: burned-area:0.1
  id: clt
  inputs:
    inp1:
      inputBinding:
        position: 1
        prefix: --pre_event
      type: Directory
    inp2:
      inputBinding:
        position: 2
        prefix: --post_event
      type: Directory
    inp3:
      inputBinding:
        position: 3
        prefix: --ndvi_threshold
      type: string
    inp4:
      inputBinding:
        position: 4
        prefix: --ndwi_threshold
      type: string
  outputs:
    results:
      outputBinding:
        glob: .
      type: Directory
  requirements:
    EnvVarRequirement:
      envDef:
        PATH: /opt/anaconda/envs/env_burned_area/bin:/home/fbrito/.nvm/versions/node/v10.21.0/bin:/opt/anaconda/bin:/usr/share/java/maven/bin:/opt/anaconda/bin:/opt/anaconda/envs/notebook/bin:/opt/anaconda/bin:/usr/share/java/maven/bin:/opt/anaconda/bin:/opt/anaconda/condabin:/opt/anaconda/envs/notebook/bin:/opt/anaconda/bin:/usr/lib64/qt-3.3/bin:/usr/share/java/maven/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/fbrito/.local/bin:/home/fbrito/bin:/home/fbrito/.local/bin
        PREFIX: /opt/anaconda/envs/env_burned_area
    ResourceRequirement: {}
  stderr: std.err
  stdout: std.out
- class: Workflow
  doc: Sentinel-2 burned area with NDVI/NDWI threshold
  id: burned-area
  inputs:
    ndvi_threshold:
      doc: NDVI difference threshold
      label: NDVI difference threshold
      type: string
    ndwi_threshold:
      doc: NDVI difference threshold
      label: NDVI difference threshold
      type: string
    post_event:
      doc: Sentinel-2 Level-2A pre-event acquisition
      label: Sentinel-2 Level-2A pre-event
      type: Directory
    pre_event:
      doc: Sentinel-2 Level-2A pre-event acquisition
      label: Sentinel-2 Level-2A pre-event
      type: Directory
  label: Sentinel-2 burned area
  outputs:
  - id: wf_outputs
    outputSource:
    - node_1/results
    type: Directory
  steps:
    node_1:
      in:
        inp1: pre_event
        inp2: post_event
        inp3: ndvi_threshold
        inp4: ndwi_threshold
      out:
      - results
      run: '#clt'
cwlVersion: v1.0
