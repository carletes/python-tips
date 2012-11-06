#!/usr/bin/env python

import sys


def read_file(fname):
    f = open(fname, "rt")
    # The same list comprehension, but now nested insed another list
    # comprehension with conditional clause
    values = [[float(bit) for bit in line.split()]
              for line in f
              if not line.startswith(">")]
    f.close()
    return values


def plot_values(values):
    for (lat, lon, mean, count) in values:
        print "%g %g %g %g" % (lat, lon, mean, count)


def main():
    plot_values(read_file(sys.argv[1]))


if __name__ == "__main__":
    sys.exit(main())
