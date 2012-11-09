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


class GribSloppyTest(unittest.TestCase):

    def test_get_version(self):
        version = gribapi_so.grib_get_api_version()
        self.assertEqual(10918, version)
        self.assertEqual(int, type(version))

    def test_read_file(self):
        grib_file = "regular_latlon_surface.grib1"
        # Let's read a GRIB file!
        with open(grib_file, "rb") as f:
            grib_message = f.read()
        grib_message_length = os.stat(grib_file).st_size

        # Get a handle ...
        h = grib_handle_new_from_message_copy(None,
                                              grib_message,
                                              grib_message_length)
        # Voila!
        self.assertIsNotNone(h)


if __name__ == "__main__":
    unittest.main()
