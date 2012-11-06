#!/usr/bin/env python

import sys


# We define a function which reads values from a file ...
def read_file(fname):
    values = []
    f = open(fname, "rt")
    for line in f:
        if not line.startswith(">"):
            read_values = []
            for bit in line.split():
                read_values.append(float(bit))
            values.append(read_values)
    f.close()
    return values


# ... and another function which plots a list of values ...
def plot_values(values):
    for (lat, lon, mean, count) in values:
        print "%g %g %g %g" % (lat, lon, mean, count)


# ... and the main function, which puts all pieces together
def main():
    plot_values(read_file(sys.argv[1]))


if __name__ == "__main__":
    sys.exit(main())
