#!/usr/bin/env python

# Some style tips: Import first the modules from the standard library ..
import sys

# .. and then yor own modules
import datafiles

# This is the syntax to import just one symbol from a module, and make it
# accessible to your code with another name
from plotting import console_plot as plot


# The function ``filter_means()`` is perhaps too specific for this particular
# script, so we keep it here.
#
# If later on, while we are writing another script to do something else, we
# realise that we could use this function, then we could move it to its own
# module, and use that module from both the new script and this one.
def filter_means(values, threshold):
    return [[lat, lon, mean, count]
            for (lat, lon, mean, count) in values
            if mean >= threshold]


def main():
    # Here we use a function from module ``datafiles``
    values = datafiles.read_metop_b_data(sys.argv[1])

    # And here we use the one we imported from ``plotting``.
    plot(filter_means(values, 15.0))


if __name__ == "__main__":
    sys.exit(main())
