import pytest
from unittest.mock import patch
from src.calculator import Calculator
from src.main import run_repl

# --- Unit Tests for Calculator Logic ---

def test_add():
    assert Calculator.add(2, 3) == 5

def test_subtract():
    assert Calculator.subtract(5, 3) == 2

def test_multiply():
    assert Calculator.multiply(2, 3) == 6

def test_divide():
    assert Calculator.divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(5, 0)

# --- Parameterized Tests ---

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0),
    (2.5, 2.5, 5.0)
])
def test_add_parameterized(a, b, expected):
    assert Calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (10, 2, 5),
    (5, 2, 2.5)
])
def test_divide_parameterized(a, b, expected):
    assert Calculator.divide(a, b) == expected

# --- REPL Integration Tests ---

def test_repl_quit(capsys):
    """Test that the REPL exits gracefully."""
    with patch('builtins.input', side_effect=['quit']):
        run_repl()
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out

def test_repl_valid_addition(capsys):
    """Test a full addition flow."""
    inputs = ['+', '5', '10', 'exit']
    with patch('builtins.input', side_effect=inputs):
        run_repl()
    captured = capsys.readouterr()
    assert "Result: 15.0" in captured.out

def test_repl_invalid_operation(capsys):
    """Test handling of invalid operation symbols."""
    inputs = ['invalid', 'exit']
    with patch('builtins.input', side_effect=inputs):
        run_repl()
    captured = capsys.readouterr()
    assert "Invalid operation" in captured.out

def test_repl_invalid_number_input(capsys):
    """Test handling of non-numeric input (Input Validation)."""
    # Inputs: operation, bad_num, good_num, good_num, exit
    inputs = ['-', 'five', '10', '2', 'exit']
    with patch('builtins.input', side_effect=inputs):
        run_repl()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter a valid number." in captured.out
    assert "Result: 8.0" in captured.out

def test_repl_divide_by_zero(capsys):
    """Test that the REPL catches the ZeroDivision error gracefully."""
    inputs = ['/', '10', '0', 'exit']
    with patch('builtins.input', side_effect=inputs):
        run_repl()
    captured = capsys.readouterr()
    assert "Error: Cannot divide by zero." in captured.out

def test_repl_subtraction(capsys):
    """Test the subtraction flow in the REPL."""
    # Inputs: operation, num1, num2, exit
    inputs = ['-', '10', '3', 'exit']
    with patch('builtins.input', side_effect=inputs):
        run_repl()
    captured = capsys.readouterr()
    assert "Result: 7.0" in captured.out

def test_repl_multiplication(capsys):
    """Test the multiplication flow in the REPL."""
    # Inputs: operation, num1, num2, exit
    inputs = ['*', '3', '4', 'exit']
    with patch('builtins.input', side_effect=inputs):
        run_repl()
    captured = capsys.readouterr()
    assert "Result: 12.0" in captured.out

def test_repl_generic_exception(capsys):
    """
    Test the generic 'except Exception' block by mocking an unexpected crash.
    """
    inputs = ['+', '1', '1', 'exit']
    
    # We mock the 'add' method to raise a generic error instead of adding
    with patch.object(Calculator, 'add', side_effect=Exception("System Failure")):
        with patch('builtins.input', side_effect=inputs):
            run_repl()
            
    captured = capsys.readouterr()
    assert "An unexpected error occurred: System Failure" in captured.out