import pytest

from app.operation import add, divide, get_operation, multiply, subtract


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (-4, 6, 2),
        (1.5, 2.5, 4.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (10, 4, 6),
        (3, 9, -6),
        (1.5, 0.5, 1.0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (5, 4, 20),
        (-3, 7, -21),
        (2.5, 2, 5.0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (20, 5, 4),
        (7, 2, 3.5),
        (-9, 3, -3),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(8, 0)


@pytest.mark.parametrize(
    ("symbol", "function"),
    [
        ("+", add),
        ("-", subtract),
        ("*", multiply),
        ("/", divide),
    ],
)
def test_get_operation(symbol, function):
    assert get_operation(symbol) == function


def test_get_operation_rejects_unknown_symbol():
    with pytest.raises(ValueError, match="Unknown operation"):
        get_operation("%")
