import ctypes
import unittest


gribapi_so = ctypes.CDLL("libgrib_api.so")


# Let's improve the argument and return value declarations for
# ``grib_handle_new_from_message_copy()``
#
# We will define some custom types

# ``grib_context`` will represent the C type ``grib_context`` defined in
# ``grib_api.h``. We are not interested in its members (we don't even know
# them!), so we just create an opaque type:

class grib_context(ctypes.Structure):
    pass


# Ditto for ``grib_handle`` and ``FILE``
class grib_handle(ctypes.Structure):
    pass


grib_handle_new_from_message_copy = gribapi_so.grib_handle_new_from_message_copy

# Declarations are now much clearer!
grib_handle_new_from_message_copy.argtypes = [
    ctypes.POINTER(grib_context),
    ctypes.c_void_p,
    ctypes.c_long,
]
grib_handle_new_from_message_copy.restype = ctypes.POINTER(grib_handle)


class GribSloppyTest(unittest.TestCase):

    def test_get_version(self):
        version = gribapi_so.grib_get_api_version()
        self.assertEqual(10916, version)
        self.assertEqual(int, type(version))

    def test_read_file(self):
        with self.assertRaises(TypeError) as exc:
            grib_handle_new_from_message_copy()
        self.assertEqual("this function takes at least 3 arguments (0 given)",
                         exc.exception.message)


if __name__ == "__main__":
    unittest.main()
