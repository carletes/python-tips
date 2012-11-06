#!/usr/bin/env python

import sys


def read_file(fname):
    values = []
    f = open(fname, "rt")
    for line in f:
        if not line.startswith(">"):
            # Improvement: List comprehension
            values.append([float(bit) for bit in line.split()])
    f.close()
    return values


def plot_values(values):
    for (lat, lon, mean, count) in values:
        print "%g %g %g %g" % (lat, lon, mean, count)


def main():
    plot_values(read_file(sys.argv[1]))


if __name__ == "__main__":
    sys.exit(main())
