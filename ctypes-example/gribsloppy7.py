import ctypes
import os
import unittest


__all__ = [
    "GribFile",
]


gribapi_so = ctypes.CDLL("libgrib_api.so")


class grib_context(ctypes.Structure):
    pass


class grib_handle(ctypes.Structure):
    pass


# grib_handle* grib_handle_new_from_message_copy(grib_context *c, void *data, size_t *length)
grib_handle_new_from_message_copy = gribapi_so.grib_handle_new_from_message_copy
grib_handle_new_from_message_copy.argtypes = [
    ctypes.POINTER(grib_context),
    ctypes.c_void_p,
    ctypes.c_long,
]
grib_handle_new_from_message_copy.restype = ctypes.POINTER(grib_handle)

# int grib_handle_delete(grib_handle *h)
grib_handle_delete = gribapi_so.grib_handle_delete
grib_handle_delete.argtypes = [
     ctypes.POINTER(grib_handle),
]
grib_handle_delete.restype = ctypes.c_int

# int grib_get_double(grib_handle *h, const char *key, double *value)
grib_get_double = gribapi_so.grib_get_double
grib_get_double.argtypes = [
    ctypes.POINTER(grib_handle),
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_double),
]
grib_get_double.restype = ctypes.c_int

# int grib_get_long(grib_handle *h, const char *key, long *value)
grib_get_long = gribapi_so.grib_get_long
grib_get_long.argtypes = [
    ctypes.POINTER(grib_handle),
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_long),
]
grib_get_long.restype = ctypes.c_int


# Let's build a nice Python wrapper
class GribFile(object):

    """A context manager representing a GRIB file object.

    """

    def __init__(self, fname):
        self.fname = fname
        self._handle = None

    def __enter__(self):
        with open(self.fname, "rb") as f:
            msg = f.read()
        msg_len = os.stat(self.fname).st_size
        self._handle = grib_handle_new_from_message_copy(None, msg, msg_len)
        return self

    def __exit__(self, *exc_info):
        grib_handle_delete(self._handle)
        self._handle = None

    def get_double(self, key):
        """Get a double value from a key, if several keys of the same name are
        present, the last one is returned.

        """
        if self._handle is None:
            raise Exception("GRIB file %s not open" % (self.fname,))

        val = ctypes.c_double()
        rc = grib_get_double(self._handle, key, ctypes.byref(val))
        if rc:
            raise Exception("grib_get_long() failed: %d" % (rc,))
        return val.value

    def get_long(self, key):
        """Get a long value from a key, if several keys of the same name are
        present, the last one is returned.

        """
        if self._handle is None:
            raise Exception("GRIB file %s not open" % (self.fname,))

        val = ctypes.c_long()
        rc = grib_get_long(self._handle, key, ctypes.byref(val))
        if rc:
            raise Exception("grib_get_long() failed: %d" % (rc,))
        return val.value


class GribFileTest(unittest.TestCase):

    def test_incorrect_usage(self):
        g = GribFile("regular_latlon_surface.grib1")

        with self.assertRaises(Exception) as exc:
            g.get_long("Ni")
        self.assertEqual("GRIB file regular_latlon_surface.grib1 not open",
                         exc.exception.message)

        with self.assertRaises(Exception) as exc:
            g.get_double("latitudeOfFirstGridPointInDegrees")
        self.assertEqual("GRIB file regular_latlon_surface.grib1 not open",
                         exc.exception.message)

    def test_read_file(self):
        # Calls are much simpler now!
        #
        # This is pretty much like
        #
        #     http://ecmwf.int/publications/manuals/grib_api/get_8c-example.html
        with GribFile("regular_latlon_surface.grib1") as g:
            self.assertEqual(16, g.get_long("Ni"))
            self.assertEqual(31, g.get_long("Nj"))
            self.assertEqual(60.0,
                             g.get_double("latitudeOfFirstGridPointInDegrees"))
            self.assertEqual(0.0,
                             g.get_double("longitudeOfFirstGridPointInDegrees"))
            self.assertEqual(0.0,
                             g.get_double("latitudeOfLastGridPointInDegrees"))
            self.assertEqual(30.0,
                             g.get_double("longitudeOfLastGridPointInDegrees"))
            self.assertEqual(2.0,
                             g.get_double("jDirectionIncrementInDegrees"))
            self.assertEqual(2.0,
                             g.get_double("iDirectionIncrementInDegrees"))


if __name__ == "__main__":
    unittest.main()
