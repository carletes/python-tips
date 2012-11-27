"""Instrument definitiions.

"""

import os
import urllib2

import logging


__all__ = [
    "AMSU",
    "ASCAT",
    "AVHRR",
    "HIRS",
    "IASI",
    "MHS",
]



def url_for(satellite, param):
    return ("https://raw.github.com/carletes/python-tips/master/data/%s/%s" %
            (satellite, param))


class Instrument(object):
    
    """Base class for all instruments.
    
    """

    description = None

    params = None

    log = logging.getLogger("instruments")

    def __init__(self, name):
        self.name = name

    def measurements(self):
        """Returns a list of tuples of the following form:

            (param, lat, lon, value)

        """
        raise NotImplementedError("Method not overriden!")

    def __str__(self):
        return "%s (%s)" % (self.name, self.description)


class ATOVS(Instrument):

    description = "Advanced TIROS Operational Vertical Sounder"

    def measurements(self):
        ret = []
        for p in self.params:
            self.log.debug("Retrieving %s data for %s", self.name, p)
            url = url_for(self.name, p)
            self.log.debug("%s: Fetching %s data from %s", self.name, p, url)
            for line in urllib2.urlopen(url):
                lat, lon, value = [float(v) for v in line.split()]
                ret.append((p, lat, lon, value))


class AMSU(ATOVS):
    
    description = "Advanced Microwave Sounding Unit"

    params = ["temperature", "humidity"]


class AVHRR(Instrument):

    description = "Advanced Very High Resolution Radiometer"

    params = ["cloud_cover", "surface_temperature", "ice_cover", "snow_cover"]


class HIRS(Instrument):

    description = "High Resolution Infra-red Sounder"

    params = ["incident_radiation"]

    def measurements(self):
        ret = []
        for p in self.params:
            self.log.debug("Retrieving %s data for %s", self.name, p)
            fname = os.path.join(os.path.dirname(__file__),
                                 "data", self.name, p)
            self.log.debug("%s: Fetching %s data from %s", self.name, p,
                           fname)
            with open(fname, "rt") as f:
                for line in f:
                    lat, lon, value = [float(v) for v in line.split()]
                    ret.append((p, lat, lon, value))


class IASI(Instrument):

    description = "Infrared Atmospheric Sounding Interferometer"

    params = ["temperature", "humidity", "surface_temperature"]


class MHS(Instrument):

    description = "Microwave Humidity Sounder"

    params = ["temperature", "humidity"]


class ASCAT(Instrument):

    description = "Advanced SCATterometer"

    params = ["wind"]
