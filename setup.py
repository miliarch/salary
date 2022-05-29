from setuptools import setup, find_packages
setup(
    name="salary",
    version="0.1",
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[],
    author='Marcus Bowman',
    author_email='miliarch.mb@gmail.com',
    description='A python module for modeling and converting salary/income information',
    license='MIT',
    keywords='salary income convert model',
    url='https://github.com/miliarch/salary',
    project_urls={
        'Source Code': 'https://github.com/miliarch/salary',
    },
    entry_points={
        'console_scripts': ['salary=salary.interface:main']
    }
)
