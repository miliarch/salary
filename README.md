# Salary calculator module

Module for salary calculations and conversions

## Installation

Use the following command to install the `salary` module with pip:
```
pip install https://github.com/miliarch/salary.git
```

Or you can clone this repository to your system:
```
git clone https://github.com/miliarch/salary.git
```

## Usage - Salary object

Import the `Salary` class:
```
>>> from salary import Salary
```

Create a new salary object - in this example, base the salary on $15 per hour:
```
>>> s = Salary(15, 'hour')
```

Access properties (hourly, daily, etc.) as needed:
```
>>> s.hourly.decimal
Decimal('15')
>>> s.hourly.dollars
'$15.00'
>>> s.hours_in_year
2080
```

### Help and examples
```
Help on class Salary in module salary.salary:

class Salary(builtins.object)
 |  Salary(*args, **kwargs)
 |
 |  Class for calculation and conversion of salary by time period
 |
 |  Methods defined here:
 |
 |  __init__(self, *args, **kwargs)
 |      Salary initialization
 |
 |      Arguments:
 |          args[0]: required: salary amount (float)
 |          args[1]: required: salary amount period (string)
 |                   valid options: [hour|day|week|fortnight|month|quarter|semester|year]
 |
 |      Keyword arguments:
 |          kwargs['hours']: custom hours in year (int) (default: 2080)
 |          kwargs['days']: custom days in year (int) (default: 260)
 |          kwargs['weeks']: custom weeks in year (int) (default: 52)
 |          kwargs['fortnights']: custom fortnights in year (int) (default: 26)
 |          kwargs['months']: custom months in year (int) (default: 12)
 |          kwargs['quarters']: custom quarters in year (int) (default: 4)
 |          kwargs['semesters']: custom semesters in year (int) (default: 2)
 |
 |      Examples:
 |          Salary(15, 'hour')
 |          Salary(31200, 'year')
 |          Salary(15, 'hour', hours=1040, days=130, weeks=26)
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  __str__(self)
 |      Return str(self).
 |
 |  per_period(self, amount, period, operation=<built-in function truediv>)
 |      Calculate amount per given period using operation callback function
 |
 |      Parameters:
 |          amount: required: the amount to base calculation on (Decimal)
 |          period: required: the period to use for the calculation (str)
 |          operation: optional: which operator to use against (amount, period) (function)
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties defined here:
 |
 |  daily
 |
 |  fortnightly
 |
 |  hourly
 |
 |  monthly
 |
 |  quarterly
 |
 |  semesterly
 |
 |  weekly
 |
 |  yearly
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
```

## Usage - command line interface

The command line interface is mainly for demonstration purposes. If you find it helpful, feel free to use it.

The `salary` entrypoint uses a similar convention to passing arguments in during a new Salary object instantiation.

### Examples:
```
$ salary 15 hour
Hourly         : $15.00
Daily          : $120.00
Weekly         : $600.00
Fortnightly    : $1,200.00
Monthly        : $2,600.00
Quarterly      : $7,800.00
Semesterly     : $15,600.00
Yearly         : $31,200.00
```

```
$ salary 15 hour hours=1500
Hourly         : $15.00
Daily          : $86.54
Weekly         : $432.69
Fortnightly    : $865.38
Monthly        : $1,875.00
Quarterly      : $5,625.00
Semesterly     : $11,250.00
Yearly         : $22,500.00
```