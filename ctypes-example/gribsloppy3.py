import ctypes
import unittest


gribapi_so = ctypes.CDLL("libgrib_api.so")


# Let's tell ``ctypes`` what kind of arguments our
# ``grib_handle_new_from_message_copy()`` expects:

# First we assign the C symbol to a Python variable, to make its usage more
# convenient ...
grib_handle_new_from_message_copy = gribapi_so.grib_handle_new_from_message_copy

# ... And then we declare the arguments it expects
grib_handle_new_from_message_copy.argtypes = [
    ctypes.c_void_p,  # grib_context *c
    ctypes.c_void_p,  #   const void *data
    ctypes.c_long,    #       size_t  data_len
]

# We should also tell ``ctypes`` the expected type of the return value of
# ``grib_handle_new_from_message_copy()``:
grib_handle_new_from_message_copy.restype = ctypes.c_void_p  #  grib_handle *


class GribSloppyTest(unittest.TestCase):

    def test_get_version(self):
        version = gribapi_so.grib_get_api_version()
        self.assertEqual(10918, version)
        self.assertEqual(int, type(version))

    def test_read_file(self):
        # This will still fail, but not with a segmentation fault!
        with self.assertRaises(TypeError) as exc:
            grib_handle_new_from_message_copy()
        self.assertEqual("this function takes at least 3 arguments (0 given)",
                         exc.exception.message)


if __name__ == "__main__":
    unittest.main()
