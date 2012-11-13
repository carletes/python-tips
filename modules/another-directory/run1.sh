#!/bin/sh

set -x

# If we try to run the script upstairs, it works: By default, Python will also
# look for all modules in the same directory

python ../script1.py ../data.txt
