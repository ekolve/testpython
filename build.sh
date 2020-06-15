#!/bin/bash

if [[ $(git rev-parse --is-shallow-repository) == 'true' ]]; then
    git fetch --unshallow
    git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"
    git fetch origin
fi;
env
