"""Satellite definitions.

"""

import logging

import instruments


__all__ = [
    "MetOp",
    "NOAA",
]


class Satellite(object):

    log = logging.getLogger("satellites")

    def __init__(self, name, instruments):
        self.name = name
        self.instruments = instruments

    def acquire(self):
        measurements = {}
        for i in self.instruments:
            self.log.debug("%s: Acquiring measurements from instument %s",
                           self.name, i.name)
            for m in i.measurements():
                param, lat, lon ,value = m
                measurements.setdefault(m, []).append((lat, lon, value))
        return measurements

    def __str__(self):
        return self.name


class MetOp(Satellite):

    def __init__(self, name):
        instr = [
            instruments.AMSU("AMSU-A"),
            instruments.AVHRR("AVHRR/3"),
            instruments.HIRS("HIRS/4"),
            instruments.MHS("MHS"),
            instruments.IASI("IASI"),
            instruments.ASCAT("ASCAT"),
        ]
        super(MetOp, self).__init__(name, instr)


class NOAA(Satellite):

    def __init__(self, name):
        instr = [
            instruments.AMSU("AMSU-A1"),
            instruments.AMSU("AMSU-A2"),
            instruments.AVHRR("AVHRR/3"),
            instruments.HIRS("HIRS/4"),
            instruments.MHS("MHS"),
        ]
        super(NOAA, self).__init__(name, instr)
