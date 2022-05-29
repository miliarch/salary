class Salary:

    _period_to_yearly_occurrences = {
        'hour': 2080,
        'day': 365,
        'week': 52,
        'fortnight': 26,
        'month': 12,
        'year': 1,
    }

    def __init__(self, *args, **kwargs):
        """ Instantiate Salary

        Arguments:
           args[0]: required: salary amount (float)
           args[1]: optional: salary amount period (string) (default: 'hour')
           args[2]: optional: salary amount yearly occurrences (int) (default: 2080)
        """
        try:
            self.amount = float(args[0])
        except (IndexError, ValueError) as err:
            # No arg provided or cannot cast value as float - raise
            raise err

        try:
            if args[1] in self._period_to_yearly_occurrences:
                self.amount_period = args[1]
            else:
                # Arg isn't allowed - set to default value
                self.amount_period = list(self._period_to_yearly_occurrences)[0]
        except IndexError:
            # No arg provided - set to default value
            self.amount_period = list(self._period_to_yearly_occurrences)[0]

        try:
            if args[1] in self._period_to_yearly_occurrences:
                self.amount_yearly_occurrences = int(args[2])
            else:
                self.amount_yearly_occurrences = self._period_to_yearly_occurrences[self.amount_period]
        except (IndexError, ValueError):
            # No arg provided or cannot cast value as int - set to default value
            self.amount_yearly_occurrences = self._period_to_yearly_occurrences[self.amount_period]

    def __repr__(self):
        return f"{self.yearly}"

    def per_period(self, period=None):
        period = self.amount_period if period == None else period
        if period == self.amount_period and self.amount_yearly_occurrences != self._period_to_yearly_occurrences[period]:
            return self.amount
        else:
            return round(self.yearly / self._period_to_yearly_occurrences[period], 2)

    @property
    def yearly(self):
        return self.amount * self.amount_yearly_occurrences

    @property
    def hourly(self):
        return self.per_period('hour')

    @property
    def daily(self):
        return self.per_period('day')

    @property
    def weekly(self):
        return self.per_period('week')

    @property
    def fortnightly(self):
        return self.per_period('fortnight')

    @property
    def monthly(self):
        return self.per_period('month')
