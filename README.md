# python-sample-project
A skeleton for new python packages

## Source Code
Goes into a directory with the package name, e.g. `sample`

## Tests
Go into a directory called `tests`.
Pytest is recommended and can be invoked anywhere in the project or `tests` directory.

## Installation
Use `pip install .` or `pip install -e .` in the project directory.
Installation instructions are defined in `setup.py`

## Development
Consider creation of a poetry package with
```
poetry init
```

Use `pytest` for testing, e.g. run in project root to execute all found tests in `tests` directory

```
pytest
```

