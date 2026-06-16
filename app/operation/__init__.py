"""Arithmetic operation functions."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def get_operation(symbol):
    if symbol not in OPERATIONS:
        raise ValueError(f"Unknown operation: {symbol}")
    return OPERATIONS[symbol]
