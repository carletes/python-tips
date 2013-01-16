import ctypes
import os
import unittest


gribapi_so = ctypes.CDLL("libgrib_api.so")


class grib_context(ctypes.Structure):
    pass


class grib_handle(ctypes.Structure):
    pass


grib_handle_new_from_message_copy = gribapi_so.grib_handle_new_from_message_copy
grib_handle_new_from_message_copy.argtypes = [
    ctypes.POINTER(grib_context),
    ctypes.c_void_p,
    ctypes.c_long,
]
grib_handle_new_from_message_copy.restype = ctypes.POINTER(grib_handle)

# Let's map more functions from GRIB API:

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


class GribSloppyTest(unittest.TestCase):

    def test_get_version(self):
        version = gribapi_so.grib_get_api_version()
        self.assertEqual(10918, version)
        self.assertEqual(int, type(version))

    def test_read_file(self):
        grib_file = "regular_latlon_surface.grib1"
        with open(grib_file, "rb") as f:
            grib_message = f.read()
        grib_message_length = os.stat(grib_file).st_size

        h = grib_handle_new_from_message_copy(None,
                                              grib_message,
                                              grib_message_length)
        self.assertIsNotNone(h)

        # We want to call now ``grib_get_long()``, which expects a pointer to
        # a long.
        #
        # We declare now a Python variable ``num_points_along_parallel`` to be
        # compatible with the C type ``long`` ...
        num_points_along_parallel = ctypes.c_long(-1)

        # ... and pass it by reference to ``grib_get_long()``
        rc = grib_get_long(h, "Ni", ctypes.byref(num_points_along_parallel))

        self.assertEqual(0, rc)
        self.assertEqual(16, num_points_along_parallel.value)

        # Ditto for ``grib_get_double()``
        lat_of_first_grid_point = ctypes.c_double(-1.0)
        rc = grib_get_double(h,
                             "latitudeOfFirstGridPointInDegrees",
                             ctypes.byref(lat_of_first_grid_point))
        self.assertEqual(0, rc)
        self.assertEqual(60.0, lat_of_first_grid_point.value)


if __name__ == "__main__":
    unittest.main()
