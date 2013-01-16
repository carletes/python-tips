#!/usr/bin/env python2.7

import sys

from tools import memory_usage


# Let's define an iterator called ``my_range()``, that will behave (almost)
# like ``xrange()``
class my_range(object):

    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    # Iterators implement the ``__iter`` method, which returns the object to
    # be iterated upon --- usually itself
    def __iter__(self):
        return self

    # Iterators also implement the ``next()`` method, which returns their next
    # value
    def next(self):
        if self.current == self.limit:
            # Once iterators are exhausted, they raise  the ``StopIteration``
            # error
            raise StopIteration()

        # Otherwise they just return the next value
        ret = self.current
        self.current += 1
        return ret


def main():
    for x, y in zip(xrange(1000), my_range(1000)):
        if x != y:
            raise Exception("Oops: %d is not %d" % (x, y))

    # ``my_range()`` returns an iterator, too ...
    with memory_usage() as u:
        x = my_range(10 * 1000 * 1000)

    # ... so now there should be almost no memory increase.
    print "my_range(): %s" % (u.rss,)


if __name__ == "__main__":
    sys.exit(main())
