#!/usr/bin/env python2.7

import logging


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
        # New method to read values stored in a GRIB file
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


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                       format="%(asctime)s %(message)s")

    grib_file = GribFile("foo.grib")
    grib_file.save(
        [
            (51.43, 1.0, "123.128", 4.0),
            (40.42, 3.7, "123.128", 5.0),
        ]
    )

    values = grib_file.read()
    print values
