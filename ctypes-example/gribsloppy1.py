# ``ctypes`` is in the Python standard library
# (http://docs.python.org/2.7/library/ctypes.html)
import ctypes
import unittest


# First we load the ``libgribapi.so`` shared library:

gribapi_so = ctypes.CDLL("libgrib_api.so")


class GribSloppyTest(unittest.TestCase):

    # Something easy to start with: A call to:
    #
    #     long grib_get_api_version(void)
    #
    # ``ctypes`` translates C integers into Python ins/longs
    def test_get_version(self):
        version = gribapi_so.grib_get_api_version()
        self.assertEqual(10918, version)
        self.assertEqual(int, type(version))


if __name__ == "__main__":
    unittest.main()
