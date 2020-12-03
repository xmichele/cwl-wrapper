class: Workflow
doc: Main stage manager
id: stage-manager
label: theStage
inputs:
  myinputs:
      doc: myinputs doc
      label: myinputs label
      type: string
outputs: {}
requirements:
  SubworkflowFeatureRequirement: {}
  ScatterFeatureRequirement: {}
steps:
    custom_node:
      in:
        myinputs: myinputs
      out:
      - example_out
      run:
        class: CommandLineTool
        baseCommand: do_something
        inputs:
          myinputs:
            type: string
            inputBinding:
              prefix: --file
        outputs:
          example_out:
            type: File
            outputBinding:
              glob: hello.txt
    node_stage_in:
      in:
        custom_input: custom_node/example_out
      out: []
      run: ''