import unittest
from salary.salary import Salary

class TestSalary(unittest.TestCase):

    def test_input_amount(self):
        self.assertEqual(Salary('12.34').amount, 12.34)
        self.assertEqual(Salary(12).amount, 12.0)
        self.assertEqual(Salary(12.34).amount, 12.34)

    def test_input_amount_period(self):
        self.assertEqual(Salary(1).amount_period, 'hour')
        self.assertEqual(Salary(1, 'invalid').amount_period, 'hour')
        self.assertEqual(Salary(1, 'hour').amount_period, 'hour')
        self.assertEqual(Salary(1, 'day').amount_period, 'day')
        self.assertEqual(Salary(1, 'week').amount_period, 'week')
        self.assertEqual(Salary(1, 'fortnight').amount_period, 'fortnight')
        self.assertEqual(Salary(1, 'month').amount_period, 'month')
        self.assertEqual(Salary(1, 'year').amount_period, 'year')

    def test_input_amount_yearly_occurrences_defaults(self):
        self.assertEqual(Salary(1).amount_yearly_occurrences, 2080)
        self.assertEqual(Salary(1, 'invalid').amount_yearly_occurrences, 2080)
        self.assertEqual(Salary(1, 'invalid', 'invalid').amount_yearly_occurrences, 2080)
        self.assertEqual(Salary(1, 'hour').amount_yearly_occurrences, 2080)
        self.assertEqual(Salary(1, 'day').amount_yearly_occurrences, 365)
        self.assertEqual(Salary(1, 'week').amount_yearly_occurrences, 52)
        self.assertEqual(Salary(1, 'fortnight').amount_yearly_occurrences, 26)
        self.assertEqual(Salary(1, 'month').amount_yearly_occurrences, 12)
        self.assertEqual(Salary(1, 'year').amount_yearly_occurrences, 1)

    def test_input_amount_yearly_occurrences_overrides(self):
        self.assertEqual(Salary(1, 'hour', 1500).amount_yearly_occurrences, 1500)
        self.assertEqual(Salary(1, 'day', 20).amount_yearly_occurrences, 20)
        self.assertEqual(Salary(1, 'week', 7).amount_yearly_occurrences, 7)
        self.assertEqual(Salary(1, 'fortnight', 3).amount_yearly_occurrences, 3)
        self.assertEqual(Salary(1, 'month', 6).amount_yearly_occurrences, 6)
        self.assertEqual(Salary(1, 'year', 2).amount_yearly_occurrences, 2)

    def test_default_instantiation(self):
        salary = Salary(1234.56)

        self.assertIsNotNone(salary)
        self.assertIsNotNone(salary.amount)
        self.assertIsNotNone(salary.amount_period)
        self.assertIsNotNone(salary.amount_yearly_occurrences)

        self.assertIsInstance(salary, Salary)
        self.assertIsInstance(salary.amount, float)
        self.assertIsInstance(salary.amount_period, str)
        self.assertIsInstance(salary.amount_yearly_occurrences, int)

        self.assertEqual(salary.amount, 1234.56)
        self.assertEqual(salary.amount_period, 'hour')
        self.assertEqual(salary.amount_yearly_occurrences, 2080)

    def test_per_period_month(self):
        salary = Salary(3022.63, 'month')
        self.assertEqual(salary.per_period('hour'), 17.44)
        self.assertEqual(salary.per_period('day'), 99.37)
        self.assertEqual(salary.per_period('week'), 697.53)
        self.assertEqual(salary.per_period('fortnight'), 1395.06)
        self.assertEqual(salary.per_period('month'), 3022.63)
        self.assertEqual(salary.per_period('year'), 36271.56)

    def test_per_period_hour(self):
        salary = Salary(15, 'hour', 1040)
        self.assertEqual(salary.per_period('hour'), 15.0)
        self.assertEqual(salary.per_period('year'), 15600.0)
        self.assertEqual(salary.per_period('day'), 42.74)
        self.assertEqual(salary.per_period('week'), 300.0)
        self.assertEqual(salary.per_period('fortnight'), 600.0)
        self.assertEqual(salary.per_period('month'), 1300.0)


if __name__ == '__main__':
    unittest.main()
