# My Data Transformation Project

A Python project performing data transformations using Pandas and NumPy, structured with industry-standard practices and a CI/CD pipeline using GitHub Actions. Logging is implemented, and dependencies are managed via `requirements.txt` and `requirements-dev.txt`.

## Features

-   Data transformation script in `src/main.py` with built-in logging.
-   Runtime dependencies managed with `requirements.txt`.
-   Development dependencies managed with `requirements-dev.txt`.
-   Tool configurations in `pyproject.toml` (Ruff, Mypy, Pytest, Bandit).
-   Linting and formatting with Ruff.
-   Static type checking with Mypy.
-   Security scanning with Bandit and Safety.
-   Unit testing with Pytest and code coverage.
-   Pre-commit hooks for local quality checks.
-   Automated CI/CD pipeline deploying and running the script on AWS EC2.
-   Script logs to console and `data/data_processing.log`.

## Local Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd my_python_project
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    First, upgrade pip and install runtime dependencies:
    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
    Then, install development dependencies:
    ```bash
    pip install -r requirements-dev.txt
    ```

4.  **Install pre-commit hooks:**
    This enables the checks defined in `.pre-commit-config.yaml` to run before each `git commit`.
    ```bash
    pre-commit install
    ```

## Running the Script Locally

To execute the data transformation script:
```bash
python src/main.py