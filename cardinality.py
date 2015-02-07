
import itertools

_SENTINEL = object()


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
        g = itertools.islice(iterable, size - 1, size)
        return next(g, _SENTINEL) is not _SENTINEL


def at_most(size, iterable):
    """
    Determines whether the `iterable` contains no more than `size` items.
    """
    raise NotImplementedError()


def between(min, max, iterable):
    """
    Determines whether the `iterable` contains no more than `size` items.
    """
    raise NotImplementedError()
