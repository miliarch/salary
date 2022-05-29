import unittest
from decimal import Decimal, InvalidOperation
from salary.salary import Salary

class TestSalary(unittest.TestCase):

    def test_invalid_input_invalid_amount(self):
        with self.assertRaises(InvalidOperation):
            s = Salary('15a')

    def test_invalid_input_no_period(self):
        with self.assertRaises(IndexError):
            s = Salary(15)

    def test_invalid_input_invalid_period(self):
        with self.assertRaises(ValueError):
            s = Salary(15, 'invalid')

    def test_invalid_input_invalid_kwargs(self):
        s = Salary(15, 'hour', centuries=1)
        with self.assertRaises(AttributeError):
            s.centuries_in_year

    def test_valid_input_minimal(self):
        s1 = Salary(15, 'hour')
        s2 = Salary(15.0, 'hour')
        s3 = Salary('15', 'hour')

        self.assertIsNotNone(s1)
        self.assertIsNotNone(s2)
        self.assertIsNotNone(s3)

        self.assertIsNotNone(s1.amount)
        self.assertIsNotNone(s2.amount)
        self.assertIsNotNone(s3.amount)

        self.assertIsNotNone(s1.period)
        self.assertIsNotNone(s2.period)
        self.assertIsNotNone(s3.period)

        self.assertIsInstance(s1, Salary)
        self.assertIsInstance(s2, Salary)
        self.assertIsInstance(s3, Salary)

        self.assertIsInstance(s1.amount, Decimal)
        self.assertIsInstance(s2.amount, Decimal)
        self.assertIsInstance(s3.amount, Decimal)

        self.assertIsInstance(s1.period, str)
        self.assertIsInstance(s2.period, str)
        self.assertIsInstance(s3.period, str)

        self.assertEqual(s1.amount, 15.0)
        self.assertEqual(s2.amount, 15.0)
        self.assertEqual(s3.amount, 15.0)

        self.assertEqual(s1.period, 'hour')
        self.assertEqual(s2.period, 'hour')
        self.assertEqual(s3.period, 'hour')

    def test_default_periods_in_year(self):
        s = Salary(15, 'hour')
        self.assertEqual(s.hours_in_year, 2080)
        self.assertEqual(s.days_in_year, 260)
        self.assertEqual(s.weeks_in_year, 52)
        self.assertEqual(s.fortnights_in_year, 26)
        self.assertEqual(s.months_in_year, 12)
        self.assertEqual(s.quarters_in_year, 4)
        self.assertEqual(s.semesters_in_year, 2)
        self.assertEqual(s.years_in_year, 1)

    def test_custom_periods_in_year_year_ineffective(self):
        s = Salary(15, 'hour', years=3)
        self.assertEqual(s.years_in_year, 1)

    def test_custom_periods_in_year_full(self):
        s = Salary(15, 'hour',
                   hours=1040,
                   days=130,
                   weeks=26,
                   fortnights=13,
                   months=10,
                   quarters=2,
                   semesters=1)
        self.assertEqual(s.hours_in_year, 1040)
        self.assertEqual(s.days_in_year, 130)
        self.assertEqual(s.weeks_in_year, 26)
        self.assertEqual(s.fortnights_in_year, 13)
        self.assertEqual(s.months_in_year, 10)
        self.assertEqual(s.quarters_in_year, 2)
        self.assertEqual(s.semesters_in_year, 1)

    def test_custom_periods_in_year_partial(self):
        s1 = Salary(15, 'hour', hours=1040, days=130)
        self.assertEqual(s1.hours_in_year, 1040)
        self.assertEqual(s1.days_in_year, 130)
        self.assertEqual(s1.weeks_in_year, 52)
        self.assertEqual(s1.fortnights_in_year, 26)
        self.assertEqual(s1.months_in_year, 12)
        self.assertEqual(s1.quarters_in_year, 4)
        self.assertEqual(s1.semesters_in_year, 2)

        s2 = Salary(15600, 'year', hours=1040, days=130)
        self.assertEqual(s2.hours_in_year, 1040)
        self.assertEqual(s2.days_in_year, 130)
        self.assertEqual(s2.weeks_in_year, 52)
        self.assertEqual(s2.fortnights_in_year, 26)
        self.assertEqual(s2.months_in_year, 12)
        self.assertEqual(s2.quarters_in_year, 4)
        self.assertEqual(s2.semesters_in_year, 2)

    def test_salary_period_calculations(self):
        s1 = Salary(15, 'hour')
        self.assertEqual(s1.hourly, Decimal(15))
        self.assertEqual(s1.daily, Decimal(120))
        self.assertEqual(s1.weekly, Decimal(600))
        self.assertEqual(s1.fortnightly, Decimal(1200))
        self.assertEqual(s1.monthly, Decimal(2600))
        self.assertEqual(s1.quarterly, Decimal(7800))
        self.assertEqual(s1.semesterly, Decimal(15600))
        self.assertEqual(s1.yearly, Decimal(31200))

        s2 = Salary(15, 'hour',
                   hours=1040,
                   days=130,
                   weeks=26,
                   fortnights=13,
                   months=10,
                   quarters=2,
                   semesters=1)
        self.assertEqual(s2.hourly, Decimal(15))
        self.assertEqual(s2.daily, Decimal(120))
        self.assertEqual(s2.weekly, Decimal(600))
        self.assertEqual(s2.fortnightly, Decimal(1200))
        self.assertEqual(s2.monthly, Decimal(1560))
        self.assertEqual(s2.quarterly, Decimal(7800))
        self.assertEqual(s2.semesterly, Decimal(15600))
        self.assertEqual(s2.yearly, Decimal(15600))

        s3 = Salary(15, 'hour', hours=1040, days=130)
        self.assertEqual(s3.hourly, Decimal(15))
        self.assertEqual(s3.daily, Decimal(120))
        self.assertEqual(s3.weekly, Decimal(300))
        self.assertEqual(s3.fortnightly, Decimal(600))
        self.assertEqual(s3.monthly, Decimal(1300))
        self.assertEqual(s3.quarterly, Decimal(3900))
        self.assertEqual(s3.semesterly, Decimal(7800))
        self.assertEqual(s3.yearly, Decimal(15600))

        s4 = Salary(15600, 'year', hours=1040, days=130)
        self.assertEqual(s4.hourly, Decimal(15))
        self.assertEqual(s4.daily, Decimal(120))
        self.assertEqual(s4.weekly, Decimal(300))
        self.assertEqual(s4.fortnightly, Decimal(600))
        self.assertEqual(s4.monthly, Decimal(1300))
        self.assertEqual(s4.quarterly, Decimal(3900))
        self.assertEqual(s4.semesterly, Decimal(7800))
        self.assertEqual(s4.yearly, Decimal(15600))


if __name__ == '__main__':
    unittest.main()
