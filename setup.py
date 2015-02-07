import os
from setuptools import setup

import cardinality

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as fp:
    long_description = fp.read()

setup(
    name='cardinality',
    description="Determine and check the size of any iterable",
    long_description=long_description,
    version=cardinality.__version__,
    author="Wouter Bolsterlee",
    author_email="uws@xs4all.nl",
    url="https://github.com/wbolster/cardinality",
    py_modules=['cardinality'],
)
