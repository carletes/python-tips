#!/usr/bin/env python2.7

import logging
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
        # ``"pepe"`` is not a floating-pont number!
        values = [(51.33333, 1.0, "123.128", "pepe")]
        grib_file = GribFile("foo.grib")
        grib_file.save(values)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                       format="%(asctime)s %(message)s")
    unittest.main()
