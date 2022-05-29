from decimal import Decimal, InvalidOperation

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
            kwargs['hours']: custom hours in year (int)
            kwargs['days']: custom days in year (int)
            kwargs['weeks']: custom weeks in year (int)
            kwargs['fortnights']: custom fortnights in year (int)
            kwargs['months']: custom months in year (int)
            kwargs['quarters']: custom quarters in year (int)
            kwargs['semesters']: custom semesters in year (int)
        """
        self._init_yearly_occurrences()
        self._handle_args(args)
        self._handle_kwargs(kwargs)

    def __repr__(self):
        return f"{self.yearly}"

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

    @property
    def yearly(self):
        return self.amount * getattr(self, f'{self.period}s_in_year')

    @property
    def hourly(self):
        return self.yearly / getattr(self, 'hours_in_year')

    @property
    def daily(self):
        return self.yearly / getattr(self, 'days_in_year')

    @property
    def weekly(self):
        return self.yearly / getattr(self, 'weeks_in_year')

    @property
    def fortnightly(self):
        return self.yearly / getattr(self, 'fortnights_in_year')

    @property
    def monthly(self):
        return self.yearly / getattr(self, 'months_in_year')

    @property
    def quarterly(self):
        return self.yearly / getattr(self, 'quarters_in_year')

    @property
    def semesterly(self):
        return self.yearly / getattr(self, 'semesters_in_year')
