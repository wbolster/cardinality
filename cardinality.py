
import collections
import itertools

_SENTINEL = object()


def count(iterable):
    """
    Count the number of items that `iterable` yields.

    Like the built-in ``len()``, but works for any iterable.
    """
    if hasattr(iterable, '__len__'):
        return len(iterable)

    d = collections.deque(enumerate(iterable, 1), maxlen=1)
    return d[0][0] if d else 0


def at_least(size, iterable):
    """
    Determines whether the `iterable` contains at least `size` items.
    """
    if size < 0:
        raise ValueError("'size' must be positive (or zero)")
    elif hasattr(iterable, '__len__'):
        return len(iterable) >= size
    elif size == 0:
        iter(iterable)
        return True
    else:
        g = itertools.islice(iterable, size - 1, None)
        return next(g, _SENTINEL) is not _SENTINEL


def at_most(size, iterable):
    """
    Determines whether the `iterable` contains no more than `size` items.
    """
    if size < 0:
        raise ValueError("'size' must be positive (or zero)")
    elif hasattr(iterable, '__len__'):
        return len(iterable) <= size
    else:
        g = itertools.islice(iterable, size, None)
        return next(g, _SENTINEL) is _SENTINEL


def between(min, max, iterable):
    """
    Determines whether the `iterable` contains no more than `size` items.
    """
    raise NotImplementedError()
