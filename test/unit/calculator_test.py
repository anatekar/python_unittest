from calculator import Calculator
import unittest


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_for_integers(self):
        self.assertEqual(4, self.calc.add(2, 2), "This would fail since addition result is not "
                                                 "proper")

    def test_add_method_for_long(self):
        self.assertEqual(100000000000000000000, self.calc.add(
            100000000000000000000 - 100000000000, 100000000000))


    def test_add(self):
        self.assertEqual(10, self.calc.add(5, 5))

    def test_assertion(self):
        '''
        Some assertions cannot be caught using normal assertRaises.
        We need to use assertRaises as a context manager. The code as
        self.assertRaises(AttributeError,[].get) doesnt catch this exception

        '''
        with self.assertRaises(AttributeError):
            [].get()

    def test_name_error(self):
        """
        The way to think about it is that assertRaises can only catch exceptions if it actually
        manages to be called. If the act of preparing its arguments raises an exception,
        then assertRaises does not even run, and so cannot catch anything.
        :return:
        """
        with self.assertRaises(NameError):
            self.calc.add(x, y)


if __name__ == '__main__':
    unittest.main()
