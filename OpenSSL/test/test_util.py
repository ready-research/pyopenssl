from OpenSSL._util import exception_from_error_queue, lib
from OpenSSL.test.util import TestCase



class TestErrors(TestCase):
    def test_exception_from_error_queue_nonexistant_reason(self):
        lib.ERR_put_error(lib.ERR_LIB_EVP, 0, 1112, "", 10)
        exc = self.assertRaises(ValueError, exception_from_error_queue, ValueError)
        self.assertEqual(exc.args[0][0][2], "")
