#!/usr/bin/env python

import sys


def read_file(fname):
    f = open(fname, "rt")
    values = [[float(bit) for bit in line.split()]
              for line in f
              if not line.startswith(">")]
    f.close()
    return values


# Next step: filter out values that do not make sense.
#
# We do it in a separate function, that we define here ...
def filter_means(values, threshold):
    ret = []
    for (lat, lon, mean, count) in values:
        if mean >= threshold:
            ret.append([lat, lon, mean, count])
    return ret


def plot_values(values):
    for (lat, lon, mean, count) in values:
        print "%g %g %g %g" % (lat, lon, mean, count)


# ... and that we use here
def main():
    plot_values(filter_means(read_file(sys.argv[1]), 15.0))
    # If, later on, we change our minds and decide to plot *all* values, all
    # we have to do is to uncomment the following line:
    #
    #     plot_values(read_file(sys.argv[1]))


if __name__ == "__main__":
    sys.exit(main())
