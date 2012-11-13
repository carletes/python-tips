"""Plotting utilities.

All function in this module should accept a single parameter called
``values``, which shoud be a list of values to plot.

"""

__all__ = [
    "console_plot",
    "postscript_plot",
]


def console_plot(values):
    """Outputs the values to the console.

    """
    for (lat, lon, mean, count) in values:
        print "%g %g %g %g" % (lat, lon, mean, count)


def postscript_plot(values):
    """Produces Postscript plots of the given values.

    """
    raise NotImplementedError("Not done yet, we do not know how to use "
                              "Matplotlib yet!")
