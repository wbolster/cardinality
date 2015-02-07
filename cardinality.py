# coding: UTF-8

import collections
import itertools

_SENTINEL = object()


def count(iterable):
    """
    Count the number of items that `iterable` yields.

    Like the built-in ``len()``, but works for any iterable::

        >>> count([1, 2, 3])
        3
        >>> count(i for i in range(500))
        500
        >>> def gen():
        ...     yield 'hello'
        ...     yield 'world'
        >>> count(gen())
        2

    """
    if hasattr(iterable, '__len__'):
        return len(iterable)

    d = collections.deque(enumerate(iterable, 1), maxlen=1)
    return d[0][0] if d else 0


def at_least(size, iterable):
    """
    Check whether the `iterable` contains at least `size` items.
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
    Check whether the `iterable` contains no more than `size` items.
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
    Check whether the `iterable` contains between `min` and `max` items.

    Both `min` and `max` are _inclusive. This function is equivalent to
    the expression

    ::

        min <= cardinality.count(iterable) <= max

    … but more efficient.

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
