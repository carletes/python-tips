#!/usr/bin/env python2.7

class GribFile(object):

    def __init__(self, path):
        self.path = path

    def save(self, values):
        f = open(self.path, "wt")
        for (lat, lon, param, value) in values:
            f.write("%g %g %s %g\n" % (lat, lon, param, value))
        f.close()


grib_file = GribFile("foo.grib")
grib_file.save(
    [
        (51.43, 1.0, "123.128", 4.0),  # Reading
        (40.42, 3.7, "123.128", 5.0),  # Madrid
    ]
)
