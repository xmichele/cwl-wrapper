[![Build Status](https://travis-ci.com/EOEPCA/cwl-wrapper.svg?branch=main)](https://travis-ci.com/EOEPCA/cwl-wrapper)

<br />
<p align="center">
  <a href="https://github.com/EOEPCA/cwl-wrapper">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">CWL-WRAPPER</h3>
  <p align="center">    
    <br />
    <a href="https://eoepca.github.io/proc-ades/master/">Open Design</a>
    .
    <a href="https://github.com/EOEPCA/cwl-wrapper/issues">Report Bug</a>
    ·
    <a href="https://github.com/EOEPCA/cwl-wrapper/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Getting Started & Usage](#getting-started--usage)
  - [Installation](#Installation)
    - [Via conda](#via-conda)
    - [Development](#development)
    - [Requirements](#requirements)
    - [python requirements](#python-requirements)
  - [Configuration](#configuration)
    - [Rules](#rules)
  - [Usage](#Usage)
  - [Examples](#examples)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## About The Project


<!-- GETTING STARTED -->
## Getting Started & Usage

### Installation

#### Via conda

```bash
conda install -c eoepca cwl-wrapper
```

#### Development

Clone this reposotory, then create the conda environment with:

```bash
cd cwl-wrapper
conda env create -f environment.yml
conda activate env_cwl_wrapper
```

Use setuptools to install the project:

```bash
python setup.py install
```

Check the installation with:

```bash
cwl-wrapper --help
```

#### Requirements

- Python
- console 

#### Python requirements

- jinja2
- pyyaml
- click

### Configuration
 
The rules, that establish connections and conventions with the user's cwl, are defined in 
[the cwl-wrapper configuration file](src/cwl_wrapper/assets/rules.yaml). 

#### Rules

```yaml
parser:
  driver: cwl
```

`parser -> driver` defines the type of objects to be parsed

### Usage

The cwl-wrapper requires
* user's CWL
* 

### Examples

In questa sezione studieremo come creare e cambiare i template del cwl-wrapper:

* src/cwl_wrapper/assets/stagein.yaml
* src/cwl_wrapper/assets/stageout.yaml
* src/cwl_wrapper/assets/maincwl.yaml
 
#### [vegetation.cwl](assets/vegetation.cwl)

Default run

```yaml
$graph:
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
      input_reference2:
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
```

```shell script
python cwl-wrapper assets/vegetation.cwl  --output  assets/vegetation.wf.yaml
```

expected result is the file [vegetation.wf.yaml](assets/vegetation.wf.yaml) 

In the new file, have been added the elements:

* [General workflow](assets/vegetation.wf.yaml#L1)
    * [node_stage_in... node_stage_in_x](assets/vegetation.wf.yaml#L53-L118)
    * [on_stage](assets/vegetation.wf.yaml#L185-192)
    * [node_stage_out](assets/vegetation.wf.yaml#L119-184)
* [User CommandLineTool/vegetation-index](assets/vegetation.wf.yaml#L193-222)
* [User Workflow](assets/vegetation.wf.yaml#L223-L258)





<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/EOEPCA/proc-ades/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. 
Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the Apache-2.0 License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Terradue - [@terradue](https://twitter.com/terradue) - info@terradue.com

Project Link: [https://github.com/EOEPCA/proc-ades](https://github.com/EOEPCA/proc-ades)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* README.md is based on [this template](https://github.com/othneildrew/Best-README-Template) by 
[Othneil Drew](https://github.com/othneildrew).

