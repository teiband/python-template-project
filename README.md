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
### Poetry
Edit `pyproject.toml` or delete it and init a new poetry package with
```
poetry init
```

Install the project dependencies in a venv
```
poetry install
```

Add a dependency from a repository and provide correct branch name (master/main)
```
poetry add git+ssh://git@github.com/teiband/some-package.git#main
```
Edit `pyproject.toml` to make the package editable if required (develop option)
```
some-package = {git = "git@github.com/teiband/some-package.git", develop = true}
```

After you made changes, run

```
poetry update
```

