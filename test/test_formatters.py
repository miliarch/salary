import unittest
from decimal import Decimal
from wage import Numeric


class TestFormatters(unittest.TestCase):

    def test_numeric_invalid_input(self):
        with self.assertRaises(ValueError):
            Numeric('1a')

    def test_numeric_valid_input(self):
        n = Numeric(1)
        self.assertIsNotNone(n)
        self.assertIsInstance(n, Numeric)
        self.assertIsNotNone(n.value)
        self.assertIsInstance(n.value, Decimal)
        self.assertEqual(n.value, 1.0)

    def test_numeric_format_dollars(self):
        value = Decimal(1234.5612)
        dollars = Numeric.format_dollars(value)
        self.assertEqual(dollars, '$1,234.56')

    def test_numeric_dollars(self):
        n1 = Numeric(1.5)
        n2 = Numeric(300)
        n3 = Numeric(Decimal(1234.5612))
        self.assertIsNotNone(n1)
        self.assertIsNotNone(n2)
        self.assertIsNotNone(n3)
        self.assertIsInstance(n1.dollars, str)
        self.assertIsInstance(n2.dollars, str)
        self.assertIsInstance(n3.dollars, str)
        self.assertEqual(n1.dollars, '$1.50')
        self.assertEqual(n2.dollars, '$300.00')
        self.assertEqual(n3.dollars, '$1,234.56')

    def test_numeric_float(self):
        n1 = Numeric(1)
        n2 = Numeric(1234.5612)
        self.assertIsNotNone(n1)
        self.assertIsNotNone(n2)
        self.assertIsInstance(n1.float, float)
        self.assertIsInstance(n2.float, float)
        self.assertEqual(n1.float, 1.0)
        self.assertEqual(n2.float, 1234.5612)

    def test_numeric_int(self):
        n1 = Numeric(1)
        n2 = Numeric(1234.5612)
        self.assertIsNotNone(n1)
        self.assertIsNotNone(n2)
        self.assertIsInstance(n1.int, int)
        self.assertIsInstance(n2.int, int)
        self.assertEqual(n1.int, 1)
        self.assertEqual(n2.int, 1234)

    def test_numeric_decimal(self):
        n1 = Numeric(1)
        n2 = Numeric(1234.5612)
        self.assertIsNotNone(n1)
        self.assertIsNotNone(n2)
        self.assertIsInstance(n1.decimal, Decimal)
        self.assertIsInstance(n2.decimal, Decimal)
        self.assertEqual(n1.decimal, Decimal(1.0))
        self.assertEqual(n2.decimal, Decimal(1234.5612))


if __name__ == '__main__':
    unittest.main()
