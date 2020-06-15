#!/bin/bash
pip3 install wheel twine

if [[ $(git rev-parse --is-shallow-repository) == 'true' ]]; then
    git fetch --unshallow
    git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"
    git fetch origin
fi;

python setup.py sdist bdist_wheel --universal
twine upload --repository testpypi -u __token__ dist/*
