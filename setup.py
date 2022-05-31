from setuptools import setup, find_packages
setup(
    name="wage",
    version="0.1",
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[],
    author='Marcus Bowman',
    author_email='miliarch.mb@gmail.com',
    description='A python module for modeling and converting salary/income information',
    long_description='README.md',
    long_description_content_type="text/markdown",
    license='LICENSE.md',
    license_content_type="text/markdown"
    keywords='wage salary income convert model',
    url='https://github.com/miliarch/wage',
    project_urls={
        'Source Code': 'https://github.com/miliarch/wage',
    },
    entry_points={
        'console_scripts': ['wage=wage.interface:main']
    }
)
