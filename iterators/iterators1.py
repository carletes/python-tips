#!/usr/bin/env python2.7

import sys

from tools import memory_usage


def main():
    # ``range()`` returns a list ...
    with memory_usage() as u:
        x = range(10 * 1000 * 1000)

    # ... so in our case the memory used by this process will be quite higher
    # now.
    print "range():  %s" % (u.rss,)

    # ``xrange()``, in contrast, returns an *iterator* ...
    with memory_usage() as u:
        x = xrange(10 * 1000 * 1000)

    # ... so now there should be almost no memory increase.
    print "xrange(): %s" % (u.rss,)


if __name__ == "__main__":
    sys.exit(main())
