#!/usr/bin/env python2.7

import logging
# Unit testing support comes with Python's standard library
# (http://docs.python.org/2.7/library/unittest.html)
import unittest


class GribFile(object):

    log = logging.getLogger("gribfile")

    def __init__(self, path):
        self.path = path

    def save(self, values):
        self.log.debug("Writing %s to GRIB file %s",
                       values, self.path)
        f = open(self.path, "wt")
        for (lat, lon, param, value) in values:
            f.write("%g %g %s %g\n" % (lat, lon, param, value))
        f.close()

    def read(self):
        f = open(self.path, "rt")
        values = []
        for line in f:
            lat, lon, param, value = line.split(" ")
            lat = float(lat)
            lon = float(lon)
            value = float(value)
            self.log.debug("Read: %g %g %s %g",
                           lat, lon, param, value)
            values.append((lat, lon, param, value))
        return values


# We define here a unit test for our ``GribFile`` class
class GribFileTest(unittest.TestCase):

    # Python's unit test framework treats all methods whose name begins with
    # ``test_`` as test cases.
    def test_read_and_write(self):
        values = [(51.43, 1.0, "123.128", 4.0),
                  (40.42, 3.7, "123.128", 5.0)]
        grib_file = GribFile("foo.grib")
        grib_file.save(values)

        read_values = grib_file.read()
        # The method ``assertEqual()`` checkes whether two values are equal.
        self.assertEqual(values, read_values)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                       format="%(asctime)s %(message)s")
    unittest.main()
