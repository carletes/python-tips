#!/usr/bin/env python

import sys


def read_file(fname):
    f = open(fname, "rt")
    values = [[float(bit) for bit in line.split()]
              for line in f
              if not line.startswith(">")]
    f.close()
    return values


# List comprehension!
def filter_means(values, threshold):
    return [[lat, lon, mean, count]
            for (lat, lon, mean, count) in values
            if mean >= threshold]


def plot_values(values):
    for (lat, lon, mean, count) in values:
        print "%g %g %g %g" % (lat, lon, mean, count)


def main():
    plot_values(filter_means(read_file(sys.argv[1]), 15.0))


if __name__ == "__main__":
    sys.exit(main())
