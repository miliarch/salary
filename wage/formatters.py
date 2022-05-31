from decimal import Decimal, InvalidOperation


class Numeric:
    """ Object to store and convert a numeric value to various other formats
    """

    def __init__(self, value):
        if isinstance(value, Numeric):
            self.value = Decimal(value.decimal)
        else:
            try:
                self.value = Decimal(value)
            except (InvalidOperation):
                raise ValueError(f'Value not numeric: {value}')

    def __repr__(self):
        return f'Numeric({repr(self.decimal)})'

    def __str__(self):
        return f'{self.decimal}'

    @staticmethod
    def format_dollars(value):
        """ Convert number value to Dollars, e.g.: 12345 -> "$12,345.00" """
        return f'${value:,.2f}'

    @property
    def dollars(self):
        return self.format_dollars(self.value)

    @property
    def float(self):
        return float(self.value)

    @property
    def int(self):
        return int(self.value)

    @property
    def decimal(self):
        return Decimal(self.value)
