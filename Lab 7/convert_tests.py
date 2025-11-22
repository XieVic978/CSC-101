from convert import str_to_float
import unittest


class TestCases(unittest.TestCase):

    def test_string_to_float(self):
        string = '17.2'
        result = str_to_float(string)
        expected = 17.2
        self.assertEqual(expected, result)

    def test_string_to_float2(self):
        string = 'Hey'
        result = str_to_float(string)
        expected = None
        self.assertEqual(expected, result)

    def test_string_to_float_integer(self):
        # Test with an integer string
        result = str_to_float('42')
        self.assertEqual(42.0, result)

    def test_string_to_float_negative(self):
        # Test with negative number
        result = str_to_float('-3.14')
        self.assertEqual(-3.14, result)

    def test_string_to_float_zero(self):
        # Test with zero
        result = str_to_float('0')
        self.assertEqual(0.0, result)

    def test_string_to_float_empty(self):
        # Test with empty string
        result = str_to_float('')
        self.assertEqual(None, result)

    def test_string_to_float_negative_integer(self):
        # Test with negative integer
        result = str_to_float('-100')
        self.assertEqual(-100.0, result)

    def test_string_to_float_with_spaces(self):
        # Test with extra whitespace (Python's float() handles this)
        result = str_to_float('  3.14  ')
        self.assertEqual(3.14, result)


if __name__ == '__main__':
    unittest.main()