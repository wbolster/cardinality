
import cardinality

import pytest


def test_at_least():

    assert cardinality.at_least(0, [])
    assert cardinality.at_least(0, [1, 2])
    assert cardinality.at_least(2, [1, 2])
    assert not cardinality.at_least(3, [1, 2])

    assert cardinality.at_least(10, range(10))

    with pytest.raises(ValueError) as e:
        cardinality.at_least(-1, [])
    assert 'must be positive' in str(e.value)

    # Must be iterable
    with pytest.raises(TypeError) as e:
        cardinality.at_least(0, 12)
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
