# This multi-line string is called a ``docstring``.
#
# Docstrings document things --- in this case, it documents the purpose of the
# whole module.
#
# They have to be the first Python statement of the thing they document
# (excluding comments, like this explanation).
"""Utilities for reading different data files.

All functions defined here should take an argument called ``fname``, pointing
to the name of the file to be read.

They should all return a list of values from the file.

"""


# This is just a convention: the list ``__all__`` enumerates all the things we
# make available to other Python scripts.
__all__ = [
    "read_grib_data",
    "read_metop_b_data",
]


def read_metop_b_data(fname):
    # This is a ``docstring`` for the function ``read_metop_b_data``. It
    # explains:
    #
    #   * What the function does.
    #   * What kind of parameters it expects.
    """Reads a METOP-B data file.

    METOP-B data files contain lines of text. Each line has four numeric
    fields, separated by a space:

        <lat> <lon> <mean> <count>

    """
    f = open(fname, "rt")
    values = [[float(bit) for bit in line.split()]
              for line in f
              if not line.startswith(">")]
    f.close()
    return values


def read_grib_data(fname):
    """Reads a GRIB file.

    We don't know how to read GRIB files yet, so this function will always
    raise an error.

    """
    raise NotImplementedError("Another lesson, perhaps!")
