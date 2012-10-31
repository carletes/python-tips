#!/usr/bin/env python2.7

import logging
import unittest

# ``closing`` is already in the Python standard library
# (http://docs.python.org/2.7/library/contextlib.html#contextlib.closing)
from contextlib import closing


class GribFile(object):

    log = logging.getLogger("gribfile")

    def __init__(self, path):
        self.path = path

    def save(self, values):
        """Saves a set of  values to a GRIB file.

        ``values`` is expected to be a list of tuples of this shape:

            (``lat``, ``lon``, ``param``, ``value``)

        where:

            ``lat`` is a floating-point number
            ``lon`` is a floating-point number
            ``param`` is a string
            ``value`` is a floating-point number
        
        If any of ``lat``, ``lon``, or ``value`` is not a floating point
        number, a ``TypeError`` exception is raised.

        """
        self.log.debug("Writing %s to GRIB file %s",
                       values, self.path)
        # Automatic closing of file!
        with closing(open(self.path, "wt")) as f:
            for (lat, lon, param, value) in values:
                f.write("%g %g %s %g\n" % (lat, lon, param, value))

    def read(self):
        # Automatic closing of file!
        with closing(open(self.path, "rt")) as f:
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


class GribFileTest(unittest.TestCase):

    def test_read_and_write(self):
        values = [(51.33333, 1.0, "123.128", 4.0),
                  (40.42, 3.7, "123.128", 5.0)]
        grib_file = GribFile("foo.grib")
        grib_file.save(values)

        read_values = grib_file.read()
        for (expected, read) in zip(values, read_values):
            expected_lat, expected_lon, _, expected_value = expected
            read_lat, read_lon, _, read_value = read
            self.assertAlmostEqual(expected_lat, read_lat, places=2)

    def test_malformed_data(self):
        values = [(51.33333, 1.0, "123.128", "pepe")]
        grib_file = GribFile("foo.grib")

        with self.assertRaises(TypeError) as exc:
            grib_file.save(values)
        self.assertEqual("float argument required, not str",
                         exc.exception.message)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                       format="%(asctime)s %(message)s")
    unittest.main()
