
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
    Determine whether the `iterable` contains at least `size` items.
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
    Determine whether the `iterable` contains no more than `size` items.
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
    Determine whether the `iterable` contains no more than `size` items.
    """
    if min < 0:
        raise ValueError("'min' must be positive (or zero)")
    if min < 0:
        raise ValueError("'max' must be positive (or zero)")
    if min > max:
        raise ValueError("'min' cannot be greater than 'max'")

    if hasattr(iterable, '__len__'):
        return min <= len(iterable) <= max
    else:
        raise NotImplementedError()
