# Module 4 Professional Calculator Command-Line Application

This is my Module 4 calculator project. It is a command-line calculator written in Python. The program keeps running until the user quits, and it can add, subtract, multiply, and divide numbers.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Checks for division by zero
- REPL-style command line menu
- Modular app folders
- Calculation factory
- Calculation history
- Special commands: `help`, `history`, and `exit`
- Input validation
- LBYL and EAFP error handling examples
- Pytest tests with parameterized test cases
- GitHub Actions workflow that checks for 100% coverage

## Project Files

- `app/operation/__init__.py` has the arithmetic operation functions.
- `app/calculation/__init__.py` has the `Calculation`, `CalculationFactory`, and `CalculationHistory` classes.
- `app/calculator/__init__.py` has the command-line calculator app.
- `main.py` starts the calculator.
- `tests/test_operations.py` tests the arithmetic operations.
- `tests/test_calculations.py` tests calculations, the factory, and history.
- `tests/test_calculator_app.py` tests the REPL commands and input handling.
- `pyproject.toml` has the pytest coverage settings.
- `.github/workflows/python-app.yml` runs the tests on GitHub.
- `requirements.txt` lists the packages needed for testing.

## Set Up Locally

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the calculator:

```powershell
python main.py
```

Calculator commands:

```text
help
history
exit
```

Run the tests:

```powershell
pytest
```

The tests are set up to fail if the coverage is below 100%.

## Git and GitHub Steps

Initialize the local Git repository:

```powershell
git init
git add .
git commit -m "Create calculator project with tests"
```

Create a new empty repository on GitHub, then connect and push:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

After pushing, open the repository on GitHub and check the Actions tab to confirm the tests pass.
