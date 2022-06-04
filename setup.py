from setuptools import setup, find_packages
from pathlib import Path
BASE_DIR = Path(__file__).parent
long_description = (BASE_DIR / "README.md").read_text()
setup(
    name="wage",
    version="0.6",
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[],
    author='Marcus Bowman',
    author_email='miliarch.mb@gmail.com',
    description='A python module for modeling and converting salary/income information',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='wage salary income convert model',
    url='https://github.com/miliarch/wage',
    project_urls={
        'Source Code': 'https://github.com/miliarch/wage',
    },
    entry_points={
        'console_scripts': ['wage=wage.interface:main']
    }
)
