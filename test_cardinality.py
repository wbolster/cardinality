
import cardinality

import pytest


def generate(size):
    """Return a generator on which len() won't work."""
    for i in range(size):
        yield i


def test_at_least():

    assert cardinality.at_least(0, [])
    assert cardinality.at_least(0, [1, 2])
    assert cardinality.at_least(0, generate(0))
    assert cardinality.at_least(0, generate(2))

    assert cardinality.at_least(2, [1, 2])
    assert not cardinality.at_least(3, [1, 2])
    assert cardinality.at_least(2, generate(4))
    assert not cardinality.at_least(2, generate(1))


def test_at_least_invalid_size():
    with pytest.raises(ValueError) as e:
        cardinality.at_least(-1, [])
    assert 'must be positive' in str(e.value)


def test_at_least_non_iterable():
    with pytest.raises(TypeError) as e:
        cardinality.at_least(0, object())
    assert 'is not iterable' in str(e.value)


def test_at_most():
    assert cardinality.at_most(2, [1])
    assert cardinality.at_most(2, [1, 2])
    assert not cardinality.at_most(2, [1, 2, 3])


def test_between():
    assert cardinality.between(0, 1, [1])
    assert cardinality.between(0, 2, [1])
    assert cardinality.between(1, 1, [1])
    assert cardinality.between(1, 1, [1])

    with pytest.raises(ValueError):
        cardinality.between(12, 3, [])
