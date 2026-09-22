import pytest
from app.operations import Operations


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (-1, 1, 0),
    (0, 0, 0),
    (2.5, 0.5, 3.0),
    (-3, -7, -10),
])
def test_addition(a, b, expected):
    assert Operations.addition(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0),
    (0, 5, -5),
    (-2, -2, 0),
    (5.5, 2.5, 3.0),
])
def test_subtraction(a, b, expected):
    assert Operations.subtraction(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),
    (-2, 3, -6),
    (5, 0, 0),
    (2.5, 4, 10.0),
])
def test_multiplication(a, b, expected):
    assert Operations.multiplication(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),
    (5, 2, 2.5),
    (-9, 3, -3),
    (0, 4, 0),
])
def test_division(a, b, expected):
    assert Operations.division(a, b) == expected


@pytest.mark.parametrize("a", [1, -1, 0, 3.5])
def test_division_by_zero(a):
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        Operations.division(a, 0)