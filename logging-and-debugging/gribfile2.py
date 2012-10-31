#!/usr/bin/env python2.7

# The module ``logging`` is in Python's standard library!
# (http://docs.python.org/2.7/library/logging.html)
import logging


class GribFile(object):

    # Here we declare a logger ...
    log = logging.getLogger("gribfile")

    def __init__(self, path):
        self.path = path

    def save(self, values):
        # ... and here we use it
        self.log.debug("Writing %s to GRIB file %s",
                       values, self.path)
        f = open(self.path, "wt")
        for (lat, lon, param, value) in values:
            f.write("%g %g %s %g\n" % (lat, lon, param, value))
        f.close()


# Here we set up logging: We want all messages with priority ``DEBUG`` and
# above, and we also want to log the timestamp.
#
# We will log to stderr, but we could also log to a file, to syslog, etc ...
logging.basicConfig(level=logging.DEBUG,
                   format="%(asctime)s %(message)s")

grib_file = GribFile("foo.grib")
grib_file.save(
    [
        (51.43, 1.0, "123.128", 4.0),
        (40.42, 3.7, "123.128", 5.0),
    ]
)
