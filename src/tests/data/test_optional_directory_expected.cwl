$graph:
- class: Workflow
  doc: Main stage manager
  id: main
  inputs:
    ADES_STAGEIN_AWS_ACCESS_KEY_ID:
      type: string?
    ADES_STAGEIN_AWS_SECRET_ACCESS_KEY:
      type: string?
    ADES_STAGEIN_AWS_SERVICEURL:
      type: string?
    ADES_STAGEOUT_AWS_ACCESS_KEY_ID:
      type: string?
    ADES_STAGEOUT_AWS_PROFILE:
      type: string?
    ADES_STAGEOUT_AWS_REGION:
      type: string?
    ADES_STAGEOUT_AWS_SECRET_ACCESS_KEY:
      type: string?
    ADES_STAGEOUT_AWS_SERVICEURL:
      type: string?
    ADES_STAGEOUT_OUTPUT:
      type: string?
    aoi:
      doc: Area of interest in Well-known Text (WKT)
      id: aoi
      label: Area of interest in Well-known Text (WKT)
      type: string?
    aws_profiles_location:
      type: File?
    coreg_type:
      default: Rigid
      doc: Coregistration type
      id: coreg_type
      label: Coregistration type
      type:
        symbols:
        - None
        - Rigid
        - Elastic
        type: enum
    mask:
      doc: Optional mask
      id: mask
      label: Optional mask
      type: string?
    post_event:
      doc: Optical calibrated post-event single band asset path
      id: post_event
      label: Optical calibrated post-event single band asset path
      type: string
    pre_event:
      doc: Optical calibrated pre-event single band asset path
      id: pre_event
      label: Optical calibrated pre-event single band asset path
      type: string
    process:
      type: string
    threshold:
      default: '0.4'
      doc: Threshold value, between 0 and 1, for the detected change contouring
      id: threshold
      label: Threshold value, between 0 and 1, for the detected change contouring
      type: string
    win_size:
      default: '41'
      doc: Size, in pixels, of the sliding window used to detect changes, bigger values
        produce smoother results
      id: win_size
      label: Size, in pixels, of the sliding window used to detect changes, bigger
        values produce smoother results
      type: string
  label: macro-cwl
  outputs:
    s3_catalog_output:
      id: s3_catalog_output
      outputSource:
      - node_stage_out/s3_catalog_output
      type: string
    wf_outputs:
      outputSource:
      - node_stage_out/wf_outputs_out
      type: Directory
  requirements:
    InlineJavascriptRequirement: {}
    ScatterFeatureRequirement: {}
    SubworkflowFeatureRequirement: {}
  steps:
    node_stage_in:
      in:
        ADES_STAGEIN_AWS_ACCESS_KEY_ID: ADES_STAGEIN_AWS_ACCESS_KEY_ID
        ADES_STAGEIN_AWS_SECRET_ACCESS_KEY: ADES_STAGEIN_AWS_SECRET_ACCESS_KEY
        ADES_STAGEIN_AWS_SERVICEURL: ADES_STAGEIN_AWS_SERVICEURL
        input: pre_event
      out:
      - pre_event_out
      run:
        arguments:
        - copy
        - -v
        - -rel
        - -r
        - '4'
        - -o
        - ./
        - --harvest
        baseCommand: Stars
        class: CommandLineTool
        cwlVersion: v1.0
        doc: Run Stars for staging input data
        hints:
          DockerRequirement:
            dockerPull: terradue/stars:1.0.0-beta.11
        id: stars
        inputs:
          ADES_STAGEIN_AWS_ACCESS_KEY_ID:
            type: string?
          ADES_STAGEIN_AWS_SECRET_ACCESS_KEY:
            type: string?
          ADES_STAGEIN_AWS_SERVICEURL:
            type: string?
          input:
            type: string?
        outputs:
          pre_event_out:
            outputBinding:
              glob: .
            type: Directory
        requirements:
          EnvVarRequirement:
            envDef:
              AWS_ACCESS_KEY_ID: $(inputs.ADES_STAGEIN_AWS_ACCESS_KEY_ID)
              AWS_SECRET_ACCESS_KEY: $(inputs.ADES_STAGEIN_AWS_SECRET_ACCESS_KEY)
              AWS__ServiceURL: $(inputs.ADES_STAGEIN_AWS_SERVICEURL)
              PATH: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
          ResourceRequirement: {}
    node_stage_in_1:
      in:
        ADES_STAGEIN_AWS_ACCESS_KEY_ID: ADES_STAGEIN_AWS_ACCESS_KEY_ID
        ADES_STAGEIN_AWS_SECRET_ACCESS_KEY: ADES_STAGEIN_AWS_SECRET_ACCESS_KEY
        ADES_STAGEIN_AWS_SERVICEURL: ADES_STAGEIN_AWS_SERVICEURL
        input: post_event
      out:
      - post_event_out
      run:
        arguments:
        - copy
        - -v
        - -rel
        - -r
        - '4'
        - -o
        - ./
        - --harvest
        baseCommand: Stars
        class: CommandLineTool
        cwlVersion: v1.0
        doc: Run Stars for staging input data
        hints:
          DockerRequirement:
            dockerPull: terradue/stars:1.0.0-beta.11
        id: stars
        inputs:
          ADES_STAGEIN_AWS_ACCESS_KEY_ID:
            type: string?
          ADES_STAGEIN_AWS_SECRET_ACCESS_KEY:
            type: string?
          ADES_STAGEIN_AWS_SERVICEURL:
            type: string?
          input:
            type: string?
        outputs:
          post_event_out:
            outputBinding:
              glob: .
            type: Directory
        requirements:
          EnvVarRequirement:
            envDef:
              AWS_ACCESS_KEY_ID: $(inputs.ADES_STAGEIN_AWS_ACCESS_KEY_ID)
              AWS_SECRET_ACCESS_KEY: $(inputs.ADES_STAGEIN_AWS_SECRET_ACCESS_KEY)
              AWS__ServiceURL: $(inputs.ADES_STAGEIN_AWS_SERVICEURL)
              PATH: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
          ResourceRequirement: {}
    node_stage_in_1_2:
      in:
        ADES_STAGEIN_AWS_ACCESS_KEY_ID: ADES_STAGEIN_AWS_ACCESS_KEY_ID
        ADES_STAGEIN_AWS_SECRET_ACCESS_KEY: ADES_STAGEIN_AWS_SECRET_ACCESS_KEY
        ADES_STAGEIN_AWS_SERVICEURL: ADES_STAGEIN_AWS_SERVICEURL
        input: mask
      out:
      - mask_out
      run:
        arguments:
        - copy
        - -v
        - -rel
        - -r
        - '4'
        - -o
        - ./
        - --harvest
        baseCommand: Stars
        class: CommandLineTool
        cwlVersion: v1.0
        doc: Run Stars for staging input data
        hints:
          DockerRequirement:
            dockerPull: terradue/stars:1.0.0-beta.11
        id: stars
        inputs:
          ADES_STAGEIN_AWS_ACCESS_KEY_ID:
            type: string?
          ADES_STAGEIN_AWS_SECRET_ACCESS_KEY:
            type: string?
          ADES_STAGEIN_AWS_SERVICEURL:
            type: string?
          input:
            type: string?
        outputs:
          mask_out:
            outputBinding:
              glob: ${ if (inputs.input == "null") {return null } else {return ".";}
                }
            type:
            - null
            - Directory
        requirements:
          EnvVarRequirement:
            envDef:
              AWS_ACCESS_KEY_ID: $(inputs.ADES_STAGEIN_AWS_ACCESS_KEY_ID)
              AWS_SECRET_ACCESS_KEY: $(inputs.ADES_STAGEIN_AWS_SECRET_ACCESS_KEY)
              AWS__ServiceURL: $(inputs.ADES_STAGEIN_AWS_SERVICEURL)
              PATH: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
          ResourceRequirement: {}
    node_stage_out:
      in:
        ADES_STAGEOUT_AWS_ACCESS_KEY_ID: ADES_STAGEOUT_AWS_ACCESS_KEY_ID
        ADES_STAGEOUT_AWS_PROFILE: ADES_STAGEOUT_AWS_PROFILE
        ADES_STAGEOUT_AWS_REGION: ADES_STAGEOUT_AWS_REGION
        ADES_STAGEOUT_AWS_SECRET_ACCESS_KEY: ADES_STAGEOUT_AWS_SECRET_ACCESS_KEY
        ADES_STAGEOUT_AWS_SERVICEURL: ADES_STAGEOUT_AWS_SERVICEURL
        ADES_STAGEOUT_OUTPUT: ADES_STAGEOUT_OUTPUT
        aws_profiles_location: aws_profiles_location
        process: process
        wf_outputs: on_stage/wf_outputs
      out:
      - s3_catalog_output
      - wf_outputs_out
      run:
        arguments:
        - copy
        - -v
        - -r
        - '4'
        - -o
        - $( inputs.ADES_STAGEOUT_OUTPUT + "/" + inputs.process )
        - valueFrom: "${\n    if( !Array.isArray(inputs.wf_outputs) )\n    {\n   \
            \     return inputs.wf_outputs.path + \"/catalog.json\";\n    }\n    var\
            \ args=[];\n    for (var i = 0; i < inputs.wf_outputs.length; i++)\n \
            \   {\n        args.push(inputs.wf_outputs[i].path + \"/catalog.json\"\
            );\n    }\n    return args;\n}\n"
        baseCommand: Stars
        class: CommandLineTool
        cwlVersion: v1.0
        doc: Run Stars for staging results
        hints:
          DockerRequirement:
            dockerPull: terradue/stars:2.3.0
        id: stars
        inputs:
          ADES_STAGEOUT_AWS_ACCESS_KEY_ID:
            type: string?
          ADES_STAGEOUT_AWS_PROFILE:
            type: string?
          ADES_STAGEOUT_AWS_REGION:
            type: string?
          ADES_STAGEOUT_AWS_SECRET_ACCESS_KEY:
            type: string?
          ADES_STAGEOUT_AWS_SERVICEURL:
            type: string?
          ADES_STAGEOUT_OUTPUT:
            type: string?
          aws_profiles_location:
            type: File?
          process:
            type: string
          wf_outputs:
            type: Directory
        outputs:
          s3_catalog_output:
            outputBinding:
              outputEval: ${ return inputs.ADES_STAGEOUT_OUTPUT + "/" + inputs.process
                + "/catalog.json"; }
            type: string
          wf_outputs_out:
            outputBinding:
              glob: .
            type: Directory
        requirements:
          EnvVarRequirement:
            envDef:
              AWS_ACCESS_KEY_ID: $(inputs.ADES_STAGEOUT_AWS_ACCESS_KEY_ID)
              AWS_SECRET_ACCESS_KEY: $(inputs.ADES_STAGEOUT_AWS_SECRET_ACCESS_KEY)
              AWS__AuthenticationRegion: $(inputs.ADES_STAGEOUT_AWS_REGION)
              AWS__Region: $(inputs.ADES_STAGEOUT_AWS_REGION)
              AWS__ServiceURL: $(inputs.ADES_STAGEOUT_AWS_SERVICEURL)
              PATH: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
          InlineJavascriptRequirement: {}
          ResourceRequirement: {}
    on_stage:
      in:
        aoi: aoi
        coreg_type: coreg_type
        mask: node_stage_in_1_2/mask_out
        post_event: node_stage_in_1/post_event_out
        pre_event: node_stage_in/pre_event_out
        threshold: threshold
        win_size: win_size
      out:
      - wf_outputs
      run: '#iris-change-detection'
- baseCommand: iris-change-detection
  class: CommandLineTool
  hints:
    DockerRequirement:
      dockerPull: docker.terradue.com/iris-change-detection:dev0.5.6
  id: clt
  inputs:
    aoi:
      inputBinding:
        position: 7
        prefix: --aoi
      type: string?
    coreg_type:
      inputBinding:
        position: 6
        prefix: --coregistration
      type:
        symbols:
        - None
        - Rigid
        - Elastic
        type: enum
    mask:
      inputBinding:
        position: 3
        prefix: --mask
      type: Directory?
    post_event:
      inputBinding:
        position: 2
        prefix: --post-event
      type: Directory
    pre_event:
      inputBinding:
        position: 1
        prefix: --pre-event
      type: Directory
    threshold:
      inputBinding:
        position: 5
        prefix: --threshold
      type: string
    win_size:
      inputBinding:
        position: 4
        prefix: --win_size
      type: string
  outputs:
    results:
      outputBinding:
        glob: .
      type: Directory
  requirements:
    EnvVarRequirement:
      envDef:
        APP_DOCKER_IMAGE: docker.terradue.com/iris-change-detection:dev0.5.6
        APP_LOGGING: https://faas-ope.terradue.com/function/metrics-collect-on-demand-services-uat
        APP_NAME: iris-change-detection
        APP_PACKAGE: app-iris-change-detection.dev.0.5.6
        APP_VERSION: 0.5.6
        PATH: /srv/conda/envs/env_iris_change_detection/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/srv/conda/envs/env_iris_change_detection/bin
        _PROJECT: CPE
    ResourceRequirement: {}
  stderr: std.err
  stdout: std.out
- class: Workflow
  doc: This service performs a Change Detection using a pair of calibrated optical
    single band assets acquired from the same sensor. The output is represented by
    Structural Similarity Index maps that show the intensity of the detected changes
    in the region of interest.
  id: iris-change-detection
  inputs:
    aoi:
      doc: Area of interest in Well-known Text (WKT)
      label: Area of interest in Well-known Text (WKT)
      type: string?
    coreg_type:
      default: Rigid
      doc: Coregistration type
      label: Coregistration type
      type:
        symbols:
        - None
        - Rigid
        - Elastic
        type: enum
    mask:
      doc: Optional mask
      label: Optional mask
      type: Directory?
    post_event:
      doc: Optical calibrated post-event single band asset path
      label: Optical calibrated post-event single band asset path
      type: Directory
    pre_event:
      doc: Optical calibrated pre-event single band asset path
      label: Optical calibrated pre-event single band asset path
      type: Directory
    threshold:
      default: '0.4'
      doc: Threshold value, between 0 and 1, for the detected change contouring
      label: Threshold value, between 0 and 1, for the detected change contouring
      type: string
    win_size:
      default: '41'
      doc: Size, in pixels, of the sliding window used to detect changes, bigger values
        produce smoother results
      label: Size, in pixels, of the sliding window used to detect changes, bigger
        values produce smoother results
      type: string
  label: Change Detection Analysis (IRIS)
  outputs:
  - id: wf_outputs
    outputSource:
    - step_1/results
    type: Directory
  steps:
    step_1:
      in:
        aoi: aoi
        coreg_type: coreg_type
        mask: mask
        post_event: post_event
        pre_event: pre_event
        threshold: threshold
        win_size: win_size
      out:
      - results
      run: '#clt'
$namespaces:
  s: https://schema.org/
cwlVersion: v1.0
s:softwareVersion: 0.5.6
schemas:
- http://schema.org/version/9.0/schemaorg-current-http.rdf
