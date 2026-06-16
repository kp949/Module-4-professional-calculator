"""Command-line calculator application."""

from app.calculation import CalculationFactory, CalculationHistory
from app.operation import OPERATIONS


class CalculatorApp:
    def __init__(self, input_func=None, output_func=None):
        self.input = input_func or input
        self.output = output_func or print
        self.history = CalculationHistory()

    def show_intro(self):
        self.output("Professional Calculator")
        self.output("Type help for commands.")

    def show_help(self):
        self.output("Operations: +, -, *, /")
        self.output("Commands: help, history, exit")

    def show_history(self):
        if self.history.is_empty():
            self.output("No calculations yet.")
            return

        for item in self.history.all():
            self.output(item.description())

    def read_number(self, prompt):
        while True:
            value = self.input(prompt)
            try:
                # EAFP: try converting the input and handle the error if it fails.
                return float(value)
            except ValueError:
                self.output("Please enter a valid number.")

    def handle_command(self, command):
        command = command.strip().lower()

        if command in ("exit", "quit"):
            self.output("Goodbye!")
            return False

        if command == "help":
            self.show_help()
            return True

        if command == "history":
            self.show_history()
            return True

        if command not in OPERATIONS:
            self.output("Invalid choice. Type help to see options.")
            return True

        first_number = self.read_number("First number: ")
        second_number = self.read_number("Second number: ")

        try:
            calculation = CalculationFactory.create(command, first_number, second_number)
            result = calculation.perform()
        except ValueError as error:
            self.output(error)
            return True

        self.history.add(calculation)
        self.output(f"Result: {result}")
        return True

    def run(self):
        self.show_intro()
        keep_running = True

        while keep_running:
            command = self.input("Operation or command: ")
            keep_running = self.handle_command(command)
