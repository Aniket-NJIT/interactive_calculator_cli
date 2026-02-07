"""
Main entry point for the Calculator REPL.
"""
import sys
from src.calculator import Calculator

def get_number(prompt: str) -> float:
    """Repeatedly prompts user for a number until valid input is given."""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def run_repl():
    """Runs the Read-Eval-Print Loop."""
    calc = Calculator()
    
    print("Welcome to the Python Calculator CLI.")
    print("Type 'exit' or 'quit' to close the application.")
    
    while True:
        operation = input("\nEnter operation (+, -, *, /) or 'exit': ").strip().lower()

        if operation in ['exit', 'quit']:
            print("Goodbye!")
            break

        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = None
            if operation == '+':
                result = calc.add(num1, num2)
            elif operation == '-':
                result = calc.subtract(num1, num2)
            elif operation == '*':
                result = calc.multiply(num1, num2)
            elif operation == '/':
                result = calc.divide(num1, num2)
            
            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":  # pragma: no cover
    # 'pragma: no cover' excludes this block from coverage stats
    run_repl()