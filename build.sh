#!/bin/bash
pip3 install -e .
pip3 install twine wheel invoke requests

if [[ $(git rev-parse --is-shallow-repository) == 'true' ]]; then
    git fetch --unshallow
    git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"
    git fetch origin
fi;

invoke build-pip
invoke deploy-pip
twine upload --repository testpypi -u __token__ dist/*
