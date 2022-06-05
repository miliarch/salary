import json
import unittest
from decimal import Decimal
from wage import Salary


class TestSalary(unittest.TestCase):

    def test_invalid_input_invalid_amount(self):
        with self.assertRaises(ValueError):
            Salary('15a')

    def test_invalid_input_no_period(self):
        with self.assertRaises(IndexError):
            Salary(15)

    def test_invalid_input_invalid_period(self):
        with self.assertRaises(ValueError):
            Salary(15, 'invalid')

    def test_invalid_input_invalid_kwarg_key(self):
        s = Salary(15, 'hour', centuries=1)
        with self.assertRaises(AttributeError):
            s.centuries_in_year

    def test_invalid_input_invalid_kwarg_value(self):
        with self.assertRaises(ValueError):
            Salary(15, 'hour', hours='1a')

    def test_valid_input_minimal(self):
        s1 = Salary(15, 'hour')
        s2 = Salary(15.0, 'hour')
        s3 = Salary('15', 'hour')

        self.assertIsNotNone(s1)
        self.assertIsNotNone(s2)
        self.assertIsNotNone(s3)

        self.assertIsNotNone(s1.amount.decimal)
        self.assertIsNotNone(s2.amount.decimal)
        self.assertIsNotNone(s3.amount.decimal)

        self.assertIsNotNone(s1.period)
        self.assertIsNotNone(s2.period)
        self.assertIsNotNone(s3.period)

        self.assertIsInstance(s1, Salary)
        self.assertIsInstance(s2, Salary)
        self.assertIsInstance(s3, Salary)

        self.assertIsInstance(s1.amount.decimal, Decimal)
        self.assertIsInstance(s2.amount.decimal, Decimal)
        self.assertIsInstance(s3.amount.decimal, Decimal)

        self.assertIsInstance(s1.period, str)
        self.assertIsInstance(s2.period, str)
        self.assertIsInstance(s3.period, str)

        self.assertEqual(s1.amount.decimal, 15.0)
        self.assertEqual(s2.amount.decimal, 15.0)
        self.assertEqual(s3.amount.decimal, 15.0)

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

    def test_custom_period_value_int_casting(self):
        s = Salary(15, 'hour', hours=2075.5)
        self.assertEqual(s.hours_in_year, 2075)

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
        self.assertEqual(s1.hourly.decimal, Decimal(15))
        self.assertEqual(s1.daily.decimal, Decimal(120))
        self.assertEqual(s1.weekly.decimal, Decimal(600))
        self.assertEqual(s1.fortnightly.decimal, Decimal(1200))
        self.assertEqual(s1.monthly.decimal, Decimal(2600))
        self.assertEqual(s1.quarterly.decimal, Decimal(7800))
        self.assertEqual(s1.semesterly.decimal, Decimal(15600))
        self.assertEqual(s1.yearly.decimal, Decimal(31200))

        s2 = Salary(15, 'hour',
                    hours=1040,
                    days=130,
                    weeks=26,
                    fortnights=13,
                    months=10,
                    quarters=2,
                    semesters=1)
        self.assertEqual(s2.hourly.decimal, Decimal(15))
        self.assertEqual(s2.daily.decimal, Decimal(120))
        self.assertEqual(s2.weekly.decimal, Decimal(600))
        self.assertEqual(s2.fortnightly.decimal, Decimal(1200))
        self.assertEqual(s2.monthly.decimal, Decimal(1560))
        self.assertEqual(s2.quarterly.decimal, Decimal(7800))
        self.assertEqual(s2.semesterly.decimal, Decimal(15600))
        self.assertEqual(s2.yearly.decimal, Decimal(15600))

        s3 = Salary(15, 'hour', hours=1040, days=130)
        self.assertEqual(s3.hourly.decimal, Decimal(15))
        self.assertEqual(s3.daily.decimal, Decimal(120))
        self.assertEqual(s3.weekly.decimal, Decimal(300))
        self.assertEqual(s3.fortnightly.decimal, Decimal(600))
        self.assertEqual(s3.monthly.decimal, Decimal(1300))
        self.assertEqual(s3.quarterly.decimal, Decimal(3900))
        self.assertEqual(s3.semesterly.decimal, Decimal(7800))
        self.assertEqual(s3.yearly.decimal, Decimal(15600))

        s4 = Salary(15600, 'year', hours=1040, days=130)
        self.assertEqual(s4.hourly.decimal, Decimal(15))
        self.assertEqual(s4.daily.decimal, Decimal(120))
        self.assertEqual(s4.weekly.decimal, Decimal(300))
        self.assertEqual(s4.fortnightly.decimal, Decimal(600))
        self.assertEqual(s4.monthly.decimal, Decimal(1300))
        self.assertEqual(s4.quarterly.decimal, Decimal(3900))
        self.assertEqual(s4.semesterly.decimal, Decimal(7800))
        self.assertEqual(s4.yearly.decimal, Decimal(15600))

    def test_serialize_by_period(self):
        s = Salary(600, 'week')
        by_period = json.loads(s.serialize_by_period('hour'))
        self.assertIsNotNone(by_period)
        self.assertIsNotNone(by_period['amount'])
        self.assertIsNotNone(by_period['amount']['float'])
        self.assertIsNotNone(by_period['amount']['dollars'])
        self.assertIsNotNone(by_period['period'])
        self.assertIsInstance(by_period, dict)
        self.assertIsInstance(by_period['amount'], dict)
        self.assertIsInstance(by_period['amount']['float'], float)
        self.assertIsInstance(by_period['amount']['dollars'], str)
        self.assertIsInstance(by_period['period'], str)
        self.assertEqual(by_period['amount']['float'], 15.0)
        self.assertEqual(by_period['amount']['dollars'], '$15.00')
        self.assertEqual(by_period['period'], 'hour')

    def test_serialize_per_period_summary(self):
        s = Salary(31200, 'year')
        per_period = json.loads(s.serialize_per_period_summary())
        self.assertIsNotNone(per_period)
        self.assertIsInstance(per_period, dict)
        self.assertIsNotNone(per_period['hour'])
        self.assertIsNotNone(per_period['hour']['float'])
        self.assertIsNotNone(per_period['hour']['dollars'])
        self.assertIsNotNone(per_period['day'])
        self.assertIsNotNone(per_period['day']['float'])
        self.assertIsNotNone(per_period['day']['dollars'])
        self.assertIsNotNone(per_period['week'])
        self.assertIsNotNone(per_period['week']['float'])
        self.assertIsNotNone(per_period['week']['dollars'])
        self.assertIsNotNone(per_period['fortnight'])
        self.assertIsNotNone(per_period['fortnight']['float'])
        self.assertIsNotNone(per_period['fortnight']['dollars'])
        self.assertIsNotNone(per_period['month'])
        self.assertIsNotNone(per_period['month']['float'])
        self.assertIsNotNone(per_period['month']['dollars'])
        self.assertIsNotNone(per_period['quarter'])
        self.assertIsNotNone(per_period['quarter']['float'])
        self.assertIsNotNone(per_period['quarter']['dollars'])
        self.assertIsNotNone(per_period['semester'])
        self.assertIsNotNone(per_period['semester']['float'])
        self.assertIsNotNone(per_period['semester']['dollars'])
        self.assertIsNotNone(per_period['year'])
        self.assertIsNotNone(per_period['year']['float'])
        self.assertIsNotNone(per_period['year']['dollars'])
        self.assertEqual(per_period['hour']['float'], 15.0)
        self.assertEqual(per_period['hour']['dollars'], '$15.00')
        self.assertEqual(per_period['day']['float'], 120.0)
        self.assertEqual(per_period['day']['dollars'], '$120.00')
        self.assertEqual(per_period['week']['float'], 600.0)
        self.assertEqual(per_period['week']['dollars'], '$600.00')
        self.assertEqual(per_period['fortnight']['float'], 1200.0)
        self.assertEqual(per_period['fortnight']['dollars'], '$1,200.00')
        self.assertEqual(per_period['month']['float'], 2600.0)
        self.assertEqual(per_period['month']['dollars'], '$2,600.00')
        self.assertEqual(per_period['quarter']['float'], 7800.0)
        self.assertEqual(per_period['quarter']['dollars'], '$7,800.00')
        self.assertEqual(per_period['semester']['float'], 15600.0)
        self.assertEqual(per_period['semester']['dollars'], '$15,600.00')
        self.assertEqual(per_period['year']['float'], 31200.0)
        self.assertEqual(per_period['year']['dollars'], '$31,200.00')

    def test_per_period_summary(self):
        s = Salary(31200, 'year')
        per_period_summary = s.per_period_summary
        self.assertIsNotNone(per_period_summary)
        self.assertIsInstance(per_period_summary, dict)
        self.assertIsNotNone(per_period_summary['hour'])
        self.assertIsNotNone(per_period_summary['hour']['float'])
        self.assertIsNotNone(per_period_summary['hour']['dollars'])
        self.assertIsNotNone(per_period_summary['day'])
        self.assertIsNotNone(per_period_summary['day']['float'])
        self.assertIsNotNone(per_period_summary['day']['dollars'])
        self.assertIsNotNone(per_period_summary['week'])
        self.assertIsNotNone(per_period_summary['week']['float'])
        self.assertIsNotNone(per_period_summary['week']['dollars'])
        self.assertIsNotNone(per_period_summary['fortnight'])
        self.assertIsNotNone(per_period_summary['fortnight']['float'])
        self.assertIsNotNone(per_period_summary['fortnight']['dollars'])
        self.assertIsNotNone(per_period_summary['month'])
        self.assertIsNotNone(per_period_summary['month']['float'])
        self.assertIsNotNone(per_period_summary['month']['dollars'])
        self.assertIsNotNone(per_period_summary['quarter'])
        self.assertIsNotNone(per_period_summary['quarter']['float'])
        self.assertIsNotNone(per_period_summary['quarter']['dollars'])
        self.assertIsNotNone(per_period_summary['semester'])
        self.assertIsNotNone(per_period_summary['semester']['float'])
        self.assertIsNotNone(per_period_summary['semester']['dollars'])
        self.assertIsNotNone(per_period_summary['year'])
        self.assertIsNotNone(per_period_summary['year']['float'])
        self.assertIsNotNone(per_period_summary['year']['dollars'])
        self.assertEqual(per_period_summary['hour']['float'], 15.0)
        self.assertEqual(per_period_summary['hour']['dollars'], '$15.00')
        self.assertEqual(per_period_summary['day']['float'], 120.0)
        self.assertEqual(per_period_summary['day']['dollars'], '$120.00')
        self.assertEqual(per_period_summary['week']['float'], 600.0)
        self.assertEqual(per_period_summary['week']['dollars'], '$600.00')
        self.assertEqual(per_period_summary['fortnight']['float'], 1200.0)
        self.assertEqual(per_period_summary['fortnight']['dollars'], '$1,200.00')
        self.assertEqual(per_period_summary['month']['float'], 2600.0)
        self.assertEqual(per_period_summary['month']['dollars'], '$2,600.00')
        self.assertEqual(per_period_summary['quarter']['float'], 7800.0)
        self.assertEqual(per_period_summary['quarter']['dollars'], '$7,800.00')
        self.assertEqual(per_period_summary['semester']['float'], 15600.0)
        self.assertEqual(per_period_summary['semester']['dollars'], '$15,600.00')
        self.assertEqual(per_period_summary['year']['float'], 31200.0)
        self.assertEqual(per_period_summary['year']['dollars'], '$31,200.00')

    def test_serialize_times_per_year(self):
        s = Salary(31200, 'year')
        times_per_year = json.loads(s.serialize_times_per_year())
        self.assertIsNotNone(times_per_year)
        self.assertIsInstance(times_per_year, dict)
        self.assertIsNotNone(times_per_year['hour'])
        self.assertIsNotNone(times_per_year['day'])
        self.assertIsNotNone(times_per_year['week'])
        self.assertIsNotNone(times_per_year['fortnight'])
        self.assertIsNotNone(times_per_year['month'])
        self.assertIsNotNone(times_per_year['quarter'])
        self.assertIsNotNone(times_per_year['semester'])
        self.assertIsNotNone(times_per_year['year'])
        self.assertEqual(times_per_year['hour'], 2080)
        self.assertEqual(times_per_year['day'], 260)
        self.assertEqual(times_per_year['week'], 52)
        self.assertEqual(times_per_year['fortnight'], 26)
        self.assertEqual(times_per_year['month'], 12)
        self.assertEqual(times_per_year['quarter'], 4)
        self.assertEqual(times_per_year['semester'], 2)
        self.assertEqual(times_per_year['year'], 1)

    def test_times_per_year(self):
        s = Salary(31200, 'year')
        times_per_year = s.times_per_year
        self.assertIsNotNone(times_per_year)
        self.assertIsInstance(times_per_year, dict)
        self.assertIsNotNone(times_per_year['hour'])
        self.assertIsNotNone(times_per_year['day'])
        self.assertIsNotNone(times_per_year['week'])
        self.assertIsNotNone(times_per_year['fortnight'])
        self.assertIsNotNone(times_per_year['month'])
        self.assertIsNotNone(times_per_year['quarter'])
        self.assertIsNotNone(times_per_year['semester'])
        self.assertIsNotNone(times_per_year['year'])
        self.assertEqual(times_per_year['hour'], 2080)
        self.assertEqual(times_per_year['day'], 260)
        self.assertEqual(times_per_year['week'], 52)
        self.assertEqual(times_per_year['fortnight'], 26)
        self.assertEqual(times_per_year['month'], 12)
        self.assertEqual(times_per_year['quarter'], 4)
        self.assertEqual(times_per_year['semester'], 2)
        self.assertEqual(times_per_year['year'], 1)

    def test_serialize(self):
        s = Salary(31200, 'year')
        obj = json.loads(s.serialize())
        self.assertIsNotNone(obj)
        self.assertIsInstance(obj, dict)
        self.assertIsNotNone(obj['amount'])
        self.assertIsNotNone(obj['period'])
        self.assertIsNotNone(obj['per_period_summary'])
        self.assertIsNotNone(obj['times_per_year'])
        self.assertIsInstance(obj['per_period_summary'], dict)
        self.assertIsInstance(obj['times_per_year'], dict)
        self.assertEqual(obj['amount']['float'], 31200.0)
        self.assertEqual(obj['amount']['dollars'], '$31,200.00')
        self.assertEqual(obj['period'], 'year')


if __name__ == '__main__':
    unittest.main()
