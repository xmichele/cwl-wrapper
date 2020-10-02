# CWL-WRAPPER

- [Requirements](#requirements)
- [requirements](#requirements.txt)
- [Run](#run) 
- [Configuration file](#configuration-file)
- [Package configuration file](#configuration-file-help)
- [Configuration file details](#configuration-file-details)
- [Templates](#templates)


## Requirements

- Python
- console 

## Python requirements

- jinja2
- pyyaml
- click


## Run 


## Configuration file


### Configuration file help

```yaml
rulez:
  version: 1

parser:
  driver: cwl

onstage:
  driver: cwl

  stage_in:
    connection_node: node_stage_in
    if_scatter:
      scatterMethod: dotproduct

  on_stage:
    connection_node: on_stage

  stage_out:
    connection_node: node_stage_out


output:
  driver: cwl
  name: '-'
  type: $graph


cwl:
  Directory:
    type: Directory
    inputBinding:
      position: 1

  Directory[]:
    type: Directory[]
    inputBinding:
      position: 1

  outputBindingResult:
    command:
      outputBinding:
        glob: .
      type: Directory
    stepOut:
      type:
        items: Directory
        type: array
```

#### Configuration file details

```yaml
rulez:
  version: 1
```

`rulez -> version` defines the Rules version. Currently only version 1 is managed  

```yaml
parser:
  driver: cwl
```

`parser -> driver` defines the type of objects to be parsed

```yaml
onstage:
  driver: cwl

  stage_in:
    connection_node: node_stage_in
    if_scatter:
      scatterMethod: dotproduct

  on_stage:
    connection_node: on_stage

  stage_out:
    connection_node: node_stage_out
```

`onstage -> driver` defines the driver to use during the translation: The result must be a `CWL` format

`onstage -> stage_in` encloses all the stage in configurations

`onstage -> stage_in -> connection_node`

`onstage -> stage_in -> if_scatter`

`onstage -> stage_in -> if_scatter -> scatterMethod`

`onstage -> on_stage`

`onstage -> on_stage -> connection_node`

`stage_out -> connection_node`

```yaml
output:
  driver: cwl
  name: '-'
  type: $graph
```

`output -> driver`

`output -> name`

`output -> type`

```yaml
cwl:
  Directory:
    type: Directory
    inputBinding:
      position: 1

  Directory[]:
    type: Directory[]
    inputBinding:
      position: 1

  outputBindingResult:
    command:
      outputBinding:
        glob: .
      type: Directory
    
    stepOut:
      type:
        items: Directory
        type: array
```

template

`cwl -> Directory`

`cwl -> Directory[]`

`cwl -> outputBindingResult`

`cwl -> outputBindingResult -> command`

`cwl -> outputBindingResult -> stepOut`


## Templates

### stage in

File: `stagein.yaml` 

```yaml
class: CommandLineTool
baseCommand: echo
label:
doc: docs
inputs: {}
outputs: {}
```

### main

File: `maincwl.yaml`

```yaml
class: Workflow
doc: Main stage manager
id: stage-manager
label: theStage
inputs: []
outputs: {}

requirements:
  SubworkflowFeatureRequirement: {}
  ScatterFeatureRequirement: {}

#steps:
#  node_stage_in:
#    in: {}
#    out: []
#    run: ''
##
#  on_stage:
#    in: {}
#    out: []
#    run: ''
#
#  node_stage_out:
#    in: []
#    out: []
#    run: ''
```

### stage out

File: `stageout.yaml`

```yaml
class: CommandLineTool
baseCommand: echo
label:
doc: docs
inputs: {}
outputs: {}
```


