#!/bin/sh

set -x

# .. unless we tell Python to look for them somewhere! That's the purpose of
# the environment variable ``PYTHONPATH``

env PYTHONPATH=".." python script1.py ../data.txt
