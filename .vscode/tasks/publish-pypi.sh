#!/bin/bash
# This file was automatically generated by jinjaroot. Do not edit directly. See the .jinjaroot dir.


set -ex

.vscode/tasks/build-py-dist.sh

twine upload ./dist/*
