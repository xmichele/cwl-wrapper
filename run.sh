#!/usr/bin/env bash

#export PYTHONPATH="/Users/rdirienzo/Project/cwl-wrapper/src"
export PYTHONPATH="$PWD/src"
cwl-wrapper assets/vegetation.cwl  --output onstage.yaml
scp onstage.yaml gavi:/home/rdirienzo/Projects/cwl-wrapper

