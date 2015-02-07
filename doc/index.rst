===========
cardinality
===========

``cardinality`` is a small Python library to determine and check the size of any
iterable (lists, iterators, generators, and so on). It is intended as a useful
companion to the built-in ``itertools`` module.


Installation
============

::

  pip install cardinality


Usage
=====

The ``cardinality`` module provides these functions:

:py:func:`cardinality.count()`

  Determines the size of an iterable.

:py:func:`cardinality.at_least()`

  checks whether an iterable has a minimum size

:py:func:`cardinality.at_most()`

  Checks whether an iterable has a maximum size.

:py:func:`cardinality.between()`

  Checks whether an iterable's size is within certain bounds.

The API docs below contain usage examples for each function.

.. note::

   These functions (at least partly) consume the iterable that is passed to it,
   so don't expect the passed iterables to be useful afterwards.


API
===

.. autofunction:: cardinality.count
.. autofunction:: cardinality.at_least
.. autofunction:: cardinality.at_most
.. autofunction:: cardinality.between


Contributing
============

The source code and issue tracker for this package can be found on Github:

  https://github.com/wbolster/cardinality

License
=======

Copyright © 2015, Wouter Bolsterlee

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

* Neither the name of the author nor the names of its contributors may be used
  to endorse or promote products derived from this software without specific
  prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

*(This is the OSI approved 3-clause "New BSD License".)*
