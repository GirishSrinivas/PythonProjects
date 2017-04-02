import unittest
import mock
import ddt

from programs import function


@ddt.ddt
class TestFunctions(unittest.TestCase):

    @ddt.data((2, [mock.call(2)]),
              (5, [mock.call(2), mock.call(3)]))
    @ddt.unpack
    def test_prime(self, input, expected_calls):

        function.printdigit = mock.Mock()

        retval = function.prime(input)

        self.assertIsNone(retval)
        function.printdigit.assert_has_calls(expected_calls)



