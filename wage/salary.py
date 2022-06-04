import json
from operator import mul, truediv
from .formatters import Numeric


class Salary:
    """ Class for calculation and conversion of salary by time period """

    _period_yearly_defaults = {
        'hour': 2080,
        'day': 260,
        'week': 52,
        'fortnight': 26,
        'month': 12,
        'quarter': 4,
        'semester': 2,
        'year': 1,
    }

    def __init__(self, *args, **kwargs):
        """ Salary initialization

        Arguments:
            args[0]: required: salary amount (float)
            args[1]: required: salary amount period (string)
                     valid options: [hour|day|week|fortnight|month|quarter|semester|year]

        Keyword arguments:
            kwargs['hours']: custom hours in year (int) (default: 2080)
            kwargs['days']: custom days in year (int) (default: 260)
            kwargs['weeks']: custom weeks in year (int) (default: 52)
            kwargs['fortnights']: custom fortnights in year (int) (default: 26)
            kwargs['months']: custom months in year (int) (default: 12)
            kwargs['quarters']: custom quarters in year (int) (default: 4)
            kwargs['semesters']: custom semesters in year (int) (default: 2)

        Examples:
            Salary(15, 'hour')
            Salary(31200, 'year')
            Salary(15, 'hour', hours=1040, days=130, weeks=26)
        """
        self._init_yearly_occurrences()
        self._handle_args(args)
        self._handle_kwargs(kwargs)

    def __repr__(self):
        out_str = 'Salary('
        out_str += f"{self.amount}, '{self.period}'"
        for key in self._period_yearly_defaults:
            value = getattr(self, f'{key}s_in_year')
            if value != self._period_yearly_defaults[key]:
                out_str += f', {key}s={value}'
        out_str += ')'
        return out_str

    def __str__(self):
        return f'{self.amount.dollars} per {self.period}'

    def _init_yearly_occurrences(self):
        self.hours_in_year = self._period_yearly_defaults['hour']
        self.days_in_year = self._period_yearly_defaults['day']
        self.weeks_in_year = self._period_yearly_defaults['week']
        self.fortnights_in_year = self._period_yearly_defaults['fortnight']
        self.months_in_year = self._period_yearly_defaults['month']
        self.quarters_in_year = self._period_yearly_defaults['quarter']
        self.semesters_in_year = self._period_yearly_defaults['semester']
        self.years_in_year = self._period_yearly_defaults['year']

    def _handle_args(self, args):
        try:
            self.amount = Numeric(args[0])
        except (IndexError, ValueError) as err:
            raise err

        try:
            if args[1] in self._period_yearly_defaults:
                self.period = args[1]
            else:
                raise ValueError(f'Invalid argument provided: {args[1]}')
        except (IndexError, ValueError) as err:
            raise err

    def _handle_kwargs(self, kwargs):
        for k, v in kwargs.items():
            if k[:-1] in self._period_yearly_defaults and k[:-1] != 'year':
                setattr(self, f'{k}_in_year', int(v))

    def per_period(self, amount, period, operation=truediv):
        """ Calculate amount per given period using operation callback function

        Parameters:
            amount: required: the amount to base calculation on (Decimal)
            period: required: the period to use for the calculation (str)
            operation: optional: which operator to use against (amount, period) (function)
        """
        return Numeric(operation(amount, getattr(self, f'{period}s_in_year')))

    def serialize_per_period(self, format='float'):
        obj = {}
        for period in self._period_yearly_defaults:
            obj[period] = getattr(self.per_period(self.yearly.decimal, period), format)
        return json.dumps(obj)

    def serialize_times_per_year(self):
        obj = {}
        for period in self._period_yearly_defaults:
            obj[period] = getattr(self, f'{period}s_in_year')
        return json.dumps(obj)

    def serialize(self):
        obj = {}
        obj['amount'] = self.amount.float
        obj['period'] = self.period
        obj['per_period_numeric'] = json.loads(self.serialize_per_period(format='float'))
        obj['per_period_dollars'] = json.loads(self.serialize_per_period(format='dollars'))
        obj['times_per_year'] = json.loads(self.serialize_times_per_year())
        return json.dumps(obj)

    @property
    def yearly(self):
        return self.per_period(self.amount.decimal, self.period, operation=mul)

    @property
    def hourly(self):
        return self.per_period(self.yearly.decimal, 'hour')

    @property
    def daily(self):
        return self.per_period(self.yearly.decimal, 'day')

    @property
    def weekly(self):
        return self.per_period(self.yearly.decimal, 'week')

    @property
    def fortnightly(self):
        return self.per_period(self.yearly.decimal, 'fortnight')

    @property
    def monthly(self):
        return self.per_period(self.yearly.decimal, 'month')

    @property
    def quarterly(self):
        return self.per_period(self.yearly.decimal, 'quarter')

    @property
    def semesterly(self):
        return self.per_period(self.yearly.decimal, 'semester')
