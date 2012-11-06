#!/usr/bin/env python

import sys


def read_file(fname):
    # I would use the ``with`` statement, to keep the code cleaner (and safer)
    with open(fname, "rt") as f:
        return [[float(bit) for bit in line.split()]
                for line in f
                if not line.startswith(">")]


def plot_values(values):
    for (lat, lon, mean, count) in values:
        print "%g %g %g %g" % (lat, lon, mean, count)


def main():
    # I would define a predicate function (a function that returns true or
    # false on its input) ...
    def sensible_mean(values):
        _, _, mean, _ = values
        return mean >= 15.0

    # ... and then use the ``filter`` function, which is part of Python
    # itself, in order to filter out the values.
    plot_values(filter(sensible_mean, read_file(sys.argv[1])))


if __name__ == "__main__":
    sys.exit(main())
