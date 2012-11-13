#!/bin/sh

set -x

# If we try to run the script *here*, it fails: Python has no way to find our
# ``datafiles`` and ``plotting`` modules ...

python script1.py ../data.txt
