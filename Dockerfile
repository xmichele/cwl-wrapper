FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]
ENV BASH_ENV=~/.bashrc                                          \
    MAMBA_ROOT_PREFIX=/opt/conda                                \
    PATH=$PATH:/opt/conda/envs/env_cwl_wrapper/bin

# Install basic commands and mamba
RUN apt-get update                                                                                                          && \
    apt-get install -y ca-certificates wget bash bzip2 gcc linux-libc-dev libc6-dev curl                                    && \
    wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba --strip-components=1 && \
    ./micromamba shell init -s bash -p ~/micromamba                                                                         && \
    apt-get clean autoremove --yes                                                                                          && \
    rm -rf /var/lib/{apt,dpkg,cache,log}                                                                                    && \
    cp ./micromamba /usr/bin

COPY . /tmp

RUN micromamba create -f /tmp/environment.yml                                                                               && \
    cd /tmp                                                                                                                 && \
    /opt/conda/envs/env_cwl_wrapper/bin/python setup.py install
