import ctypes
import unittest


gribapi_so = ctypes.CDLL("libgrib_api.so")


class GribSloppyTest(unittest.TestCase):

    def test_get_version(self):
        version = gribapi_so.grib_get_api_version()
        self.assertEqual(10916, version)
        self.assertEqual(int, type(version))

    def test_read_file(self):
        # This will bomb! The C declaration of
        # ``grib_handle_new_from_message_copy`` # is:
        #
        #     grib_handle
        #     *grib_handle_new_from_message_copy(grib_context *,
        #                                        const void *data,
        #                                        size_t data_len)
        #
        # What we're about to do is the C equivalent of:
        #
        #     grib_handle_new_from_message_copy()
        #
        # (in case it were possible to do such thing!), with God knows what
        # values for the arguments.

        gribapi_so.grib_handle_new_from_message_copy()


if __name__ == "__main__":
    unittest.main()
