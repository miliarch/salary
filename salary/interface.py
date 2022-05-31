import sys
from .salary import Salary


def salary_report(salary):
    periods = [
        'hourly',
        'daily',
        'weekly',
        'fortnightly',
        'monthly',
        'quarterly',
        'semesterly',
        'yearly'
    ]

    out_str = ""
    for period in periods:
        amount = getattr(salary, period)
        out_str += f'{period.title():15}: {amount.dollars}\n'
    return out_str


def main(args=sys.argv[1:]):
    salary_args = []
    salary_kwargs = {}
    for arg in args:
        if '=' not in arg:
            salary_args.append(arg)
        else:
            k = arg.split('=')[0]
            v = arg.split('=')[1]
            salary_kwargs[k] = v
    salary = Salary(*salary_args, **salary_kwargs)
    print(salary_report(salary))


if __name__ == "__main__":
    main()
