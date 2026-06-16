import pytest

from app.calculation import Calculation, CalculationFactory, CalculationHistory


@pytest.mark.parametrize(
    ("operation", "a", "b", "expected"),
    [
        ("+", 8, 2, 10),
        ("-", 8, 2, 6),
        ("*", 8, 2, 16),
        ("/", 8, 2, 4),
    ],
)
def test_calculation_performs_operation(operation, a, b, expected):
    calculation = Calculation(operation, a, b)
    assert calculation.perform() == expected


def test_calculation_description():
    calculation = Calculation("+", 3, 4)
    assert calculation.description() == "3 + 4 = 7"


def test_calculation_factory_creates_calculation():
    calculation = CalculationFactory.create("*", 5, 6)
    assert calculation.operation == "*"
    assert calculation.first_number == 5
    assert calculation.second_number == 6
    assert calculation.perform() == 30


def test_calculation_factory_rejects_unknown_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        CalculationFactory.create("%", 5, 6)


def test_calculation_history_starts_empty():
    history = CalculationHistory()
    assert history.is_empty()
    assert history.all() == []


def test_calculation_history_stores_items():
    history = CalculationHistory()
    calculation = Calculation("-", 9, 3)

    history.add(calculation)

    assert not history.is_empty()
    assert history.all() == [calculation]
