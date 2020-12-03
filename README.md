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


### Examples



#### [vegetation.cwl](assets/vegetation.cwl)

```yaml

```







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

