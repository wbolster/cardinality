# coding: UTF-8

"""
cardinality: determine and check the size of any iterable
"""

import collections
import itertools

__version__ = '0.1.0'
__version_info__ = tuple(map(int, __version__.split('.')))

_SENTINEL = object()


__all__ = [
    'count',
    'at_least',
    'at_most',
    'between',
]


def count(iterable):
    """
    Count the number of items that `iterable` yields.

    Equivalent to the expression

    ::

      len(iterable)

    … but it also works for iterables that do not support ``len()``.

      >>> import cardinality

      >>> cardinality.count([1, 2, 3])
      3
      >>> cardinality.count(i for i in range(500))
      500
      >>> def gen():
      ...     yield 'hello'
      ...     yield 'world'
      >>> cardinality.count(gen())
      2

    """
    if hasattr(iterable, '__len__'):
        return len(iterable)

    d = collections.deque(enumerate(iterable, 1), maxlen=1)
    return d[0][0] if d else 0


def at_least(size, iterable):
    """
    Check whether `iterable` yields at least `size` items.

    Equivalent to the expression

    ::

      cardinality.count(iterable) >= size

    … but more efficient.

    ::

      >>> import cardinality

      >>> cardinality.at_least(3, range(2))
      False
      >>> cardinality.at_least(3, range(5))
      True
      >>> def gen():
      ...     yield 'hello'
      ...     yield 'world'
      >>> cardinality.at_least(2, gen())
      True

    """
    if size < 0:
        raise ValueError("'size' must be positive (or zero)")
    elif hasattr(iterable, '__len__'):
        return len(iterable) >= size
    elif size == 0:
        iter(iterable)
        return True
    else:
        # Skip first (n - 1) items. If the iterable yields anything
        # after that, we're good.
        g = itertools.islice(iterable, size - 1, None)
        return next(g, _SENTINEL) is not _SENTINEL


def at_most(size, iterable):
    """
    Check whether `iterable` yields no more than `size` items.

    Equivalent to the expression

    ::

      cardinality.count(iterable) <= size

    … but more efficient.

    ::

      >>> import cardinality

      >>> cardinality.at_most(3, range(2))
      True
      >>> cardinality.at_most(3, range(5))
      False
      >>> def gen():
      ...     yield 'hello'
      ...     yield 'world'
      >>> cardinality.at_most(1, gen())
      False

    """
    if size < 0:
        raise ValueError("'size' must be positive (or zero)")
    elif hasattr(iterable, '__len__'):
        return len(iterable) <= size
    else:
        # Skip first n items. If the iterable doesn't yield anyting
        # after that, we're good.
        g = itertools.islice(iterable, size, None)
        return next(g, _SENTINEL) is _SENTINEL


def between(min, max, iterable):
    """
    Check whether `iterable` yields at least `min` and at most `max` items.

    Equivalent to the expression

    ::

      min <= cardinality.count(iterable) <= max

    … but more efficient.

    ::

      >>> import cardinality

      >>> cardinality.between(4, 6, range(5))
      True
      >>> cardinality.between(4, 6, range(20))
      False
      >>> def gen():
      ...     yield 'hello'
      ...     yield 'world'
      >>> cardinality.between(0, 3, gen())
      True

    """
    if min < 0:
        raise ValueError("'min' must be positive (or zero)")
    if max < 0:
        raise ValueError("'max' must be positive (or zero)")
    if min > max:
        raise ValueError("'max' must be greater or equal than 'min'")

    if hasattr(iterable, '__len__'):
        return min <= len(iterable) <= max

    # Lower bound: consume (min - 1) items, then check whether the
    # iterable yields anything.
    if min > 0:
        g = itertools.islice(iterable, min - 1, None)
        if next(g, _SENTINEL) is _SENTINEL:
            return False  # too few items

    # Upper bound: check that the remainder is not too large. The block
    # above consumed exactly "min" items, so at_most() can do the rest.
    return at_most(max - min, iterable)
