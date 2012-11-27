import instruments


class Satellite(object):

    def __init__(self, name, instruments):
        self.name = name
        self.instruments = instruments

    def acquire(self):
        measurements = {}
        for i in self.instruments:
            for m in i.measurements():
                param, lat, lon ,value = m
                measurements.setdefault(m, []).append((lat, lon, value))
        return measurements


class MetOp(Satellite):

    def __init__(self, name):
        instruments = [
            instruments.AMSU("AMSU-A"),
            instruments.AVHRR("AVHRR/3"),
            instruments.HIRS("HIRS/4"),
            instruments.MHS("MHS"),
            instruments.IASI("IASI"),
            instruments.ASCAT("ASCAT"),
        ]
        super(MetOp, self).__init__(name, instuments)
