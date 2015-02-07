
import cardinality

import pytest


def generate(size):
    """Return a generator on which len() won't work."""
    for i in range(size):
        yield i


def test_count():
    assert cardinality.count([1, 2]) == 2
    assert cardinality.count(generate(0)) == 0
    assert cardinality.count(generate(3)) == 3
    assert cardinality.count(dict()) == 0


def test_at_least():
    assert cardinality.at_least(0, [])
    assert cardinality.at_least(0, [1, 2])
    assert cardinality.at_least(0, generate(0))
    assert cardinality.at_least(0, generate(2))
    assert cardinality.at_least(2, [1, 2])
    assert not cardinality.at_least(3, [1, 2])
    assert cardinality.at_least(1, generate(1))
    assert cardinality.at_least(2, generate(4))
    assert not cardinality.at_least(10, generate(2))


def test_at_most():
    assert cardinality.at_most(0, [])
    assert not cardinality.at_most(0, [1])
    assert cardinality.at_most(2, [1])
    assert cardinality.at_most(2, [1, 2])
    assert not cardinality.at_most(2, [1, 2, 3])
    assert cardinality.at_most(0, generate(0))
    assert cardinality.at_most(1, generate(0))
    assert cardinality.at_most(1, generate(1))
    assert cardinality.at_most(20, generate(10))
    assert cardinality.at_most(3, generate(3))
    assert not cardinality.at_most(2, generate(10))


def test_between():
    assert cardinality.between(0, 1, [1])
    assert cardinality.between(0, 2, [1])
    assert cardinality.between(1, 1, [1])
    assert cardinality.between(1, 1, [1])


@pytest.mark.parametrize("func", [cardinality.at_least, cardinality.at_most])
def test_invalid_size(func):
    with pytest.raises(ValueError) as e:
        func(-1, [])
    assert 'must be positive' in str(e.value)


def test_count_non_iterable():
    with pytest.raises(TypeError) as e:
        cardinality.count(object())
    assert 'is not iterable' in str(e.value)


@pytest.mark.parametrize("func", [cardinality.at_least, cardinality.at_most])
def test_non_iterable(func):
    with pytest.raises(TypeError) as e:
        func(0, object())
    assert 'is not iterable' in str(e.value)


def test_between_non_iterable():
    with pytest.raises(TypeError) as e:
        cardinality.between(0, 1, object())
    assert 'is not iterable' in str(e.value)


def test_between_invalid_range():
    with pytest.raises(ValueError) as e:
        cardinality.between(12, 3, [])
    assert 'must be greater' in str(e.value)
