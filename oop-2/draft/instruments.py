import logging


class Instrument(object):
    
    """Base class for all instruments.
    
    """

    description = None

    log = logging.getLogger("instruments")

    def __init__(self, name):
        self.name = name

    def measurements(self):
        """Returns a list of tuples of the following form:

            (param, lat, lon, value)

        """
        raise NotImplementedError("Override in derived class!")

    def __str__(self):
        return "%s (%s)" % (self.name, self.description)


class ATOVS(Instrument):

    description = "Advanced TIROS Operational Vertical Sounder"


class AMSU(ATOVS):
    
    description = "Advanced Microwave Sounding Unit"


class AVHRR(Instrument):

    description = "Advanced Very High Resolution Radiometer"


class HIRS(Instrument):

    description = "High Resolution Infra-red Sounder"


class IASI(Instrument):

    description = "Infrared Atmospheric Sounding Interferometer"


class MHS(Instrument):

    description = "Microwave Humidity Sounder"


class ASCAT(Instrument):

    description = "Advanced SCATterometer"
