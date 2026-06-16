"""Calculation classes for the calculator app."""

from dataclasses import dataclass

from app.operation import OPERATIONS, get_operation


@dataclass
class Calculation:
    operation: str
    first_number: float
    second_number: float

    def perform(self):
        operation_function = get_operation(self.operation)
        return operation_function(self.first_number, self.second_number)

    def description(self):
        return f"{self.first_number} {self.operation} {self.second_number} = {self.perform()}"


class CalculationFactory:
    @staticmethod
    def create(operation, first_number, second_number):
        # LBYL: check the operation before creating the calculation.
        if operation not in OPERATIONS:
            raise ValueError(f"Unknown operation: {operation}")
        return Calculation(operation, first_number, second_number)


class CalculationHistory:
    def __init__(self):
        self._calculations = []

    def add(self, calculation):
        self._calculations.append(calculation)

    def all(self):
        return self._calculations

    def is_empty(self):
        return len(self._calculations) == 0
