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
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
