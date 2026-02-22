#!/bin/bash

# Install PyForge: use --break-system-packages on externally managed environments.
pip3 install ../ --user "$@"
