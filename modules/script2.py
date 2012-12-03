#!/usr/bin/env python

import sys

import datafiles

# Now we decide to use a different plotting function
from plotting import postscript_plot as plot


def filter_means(values, threshold):
    return [[lat, lon, mean, count]
            for (lat, lon, mean, count) in values
            if mean >= threshold]


def main():
    values = datafiles.read_metop_b_data(sys.argv[1])

    # We do not need to change the code of our script!
    plot(filter_means(values, 15.0))


if __name__ == "__main__":
    sys.exit(main())
