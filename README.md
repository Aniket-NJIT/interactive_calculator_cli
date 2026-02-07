# Python Calculator CLI

A robust, command-line calculator application built with Python. This project demonstrates best practices in software development, including the **DRY principle**, **separation of concerns**, **dependency injection**, and **Continuous Integration (CI)** with GitHub Actions.

## Features

- **REPL Interface:** Continuous "Read-Eval-Print Loop" for seamless interaction.
- **Arithmetic Operations:** Supports Addition (`+`), Subtraction (`-`), Multiplication (`*`), and Division (`/`).
- **Robust Error Handling:** Gracefully handles:
  - Division by zero.
  - Invalid numeric inputs.
  - Unknown operations.
- **100% Test Coverage:** Verified by comprehensive unit and integration tests using `pytest`.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.10 or higher**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Pip**: The Python package installer (usually included with Python).

## Installation & Setup

Follow these steps to set up the project locally.

### 1. Clone the Repository

Open your terminal or command prompt and run the following command to download the code:

```bash
git clone https://github.com/Aniket-NJIT/interactive_calculator_cli.git
cd interactive_calculator_cli
```

### 2. Create a Virtual Environment
It is best practice to run Python projects in a virtual environment to isolate dependencies.

#### On macOS and Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
This project relies on specific external libraries for testing and code coverage. These are listed in the requirements.txt file.

The exact dependencies are:

pytest (v8.0.0+): A mature, full-featured Python testing tool.

pytest-cov (v4.1.0+): A plugin for pytest that produces coverage reports.

pluggy: A plugin manager used internally by pytest.

#### To install them all at once, run:
```bash
pip install -r requirements.txt
```

### 4. Usage
To start the calculator application, ensure your virtual environment is active and run the following command from the project root:
```bash
python -m src.main
```

### 5. Testing & Coverage
This project enforces 100% code coverage. The test suite includes:

Unit Tests: Verify the logic of individual arithmetic functions in src/calculator.py.

Integration Tests: Verify the user interface and input handling in src/main.py using Dependency Injection.

To run the tests and generate a coverage report:
```bash
pytest --cov=src --cov-report=term-missing
```

### 6. Continuous Integration (CI)
This repository uses GitHub Actions to automatically verify code quality on every push.

Workflow File: .github/workflows/ci.yml

Trigger: Pushes and Pull Requests to the main branch.

Enforcement: The build will fail if: Any test fails OR Code coverage falls below 100%.
