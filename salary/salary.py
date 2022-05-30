from decimal import Decimal, InvalidOperation
from operator import mul, truediv

class Salary:

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
        """ Instantiate Salary

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
        return f"{round(self.yearly, 2)}"

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
            self.amount = Decimal(args[0])
        except (IndexError, InvalidOperation) as err:
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
        """
        return operation(amount, getattr(self, f'{period}s_in_year'))

    @property
    def yearly(self):
        return self.per_period(self.amount, self.period, operation=mul)

    @property
    def hourly(self):
        return self.per_period(self.yearly, 'hour')

    @property
    def daily(self):
        return self.per_period(self.yearly, 'day')

    @property
    def weekly(self):
        return self.per_period(self.yearly, 'week')

    @property
    def fortnightly(self):
        return self.per_period(self.yearly, 'fortnight')

    @property
    def monthly(self):
        return self.per_period(self.yearly, 'month')

    @property
    def quarterly(self):
        return self.per_period(self.yearly, 'quarter')

    @property
    def semesterly(self):
        return self.per_period(self.yearly, 'semester')
