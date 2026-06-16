from app.calculator import CalculatorApp


def make_app(inputs):
    values = iter(inputs)
    output = []
    app = CalculatorApp(
        input_func=lambda prompt: next(values),
        output_func=lambda message: output.append(str(message)),
    )
    return app, output


def test_app_can_be_created_with_default_functions():
    app = CalculatorApp()
    assert app.history.is_empty()


def test_show_intro():
    app, output = make_app([])
    app.show_intro()
    assert output == ["Professional Calculator", "Type help for commands."]


def test_help_command():
    app, output = make_app([])
    assert app.handle_command("help")
    assert "Operations: +, -, *, /" in output
    assert "Commands: help, history, exit" in output


def test_empty_history_command():
    app, output = make_app([])
    assert app.handle_command("history")
    assert output == ["No calculations yet."]


def test_history_after_calculation():
    app, output = make_app(["2", "3"])

    assert app.handle_command("+")
    assert app.handle_command("history")

    assert "Result: 5.0" in output
    assert "2.0 + 3.0 = 5.0" in output


def test_exit_command_stops_app():
    app, output = make_app([])
    assert not app.handle_command("exit")
    assert output == ["Goodbye!"]


def test_quit_command_stops_app():
    app, output = make_app([])
    assert not app.handle_command("quit")
    assert output == ["Goodbye!"]


def test_invalid_command_keeps_app_running():
    app, output = make_app([])
    assert app.handle_command("bad command")
    assert output == ["Invalid choice. Type help to see options."]


def test_read_number_repeats_until_valid():
    app, output = make_app(["abc", "4.5"])
    assert app.read_number("Number: ") == 4.5
    assert output == ["Please enter a valid number."]


def test_division_by_zero_is_handled():
    app, output = make_app(["10", "0"])
    assert app.handle_command("/")
    assert output == ["Cannot divide by zero."]


def test_run_loop_until_exit():
    app, output = make_app(["help", "exit"])
    app.run()
    assert output == [
        "Professional Calculator",
        "Type help for commands.",
        "Operations: +, -, *, /",
        "Commands: help, history, exit",
        "Goodbye!",
    ]
