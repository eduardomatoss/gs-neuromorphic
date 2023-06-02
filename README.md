# gs-neuromorphic

Project developed for the Global Solution of the discipline of Neuromorphic Computing and Supercomputers


[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-31011/)
[![PEP20](https://img.shields.io/badge/code%20style-pep20-red.svg)](https://www.python.org/dev/peps/pep-0020/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![bandit](https://img.shields.io/badge/code%20style-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Technology and Resources

- [Python 3.10](https://www.python.org/downloads/release/python-31011/) - **pre-requisite**
- [Docker](https://www.docker.com/get-started) - **pre-requisite**
- [Docker Compose](https://docs.docker.com/compose/) - **pre-requisite**
- [Poetry](https://python-poetry.org/)
- [Streamlit](https://streamlit.io/)

## Running Docker

### How to Build Docker

```
make docker/build
```

### How to Run

```
make docker/run
```

### Recommended command to running the application

```
make docker/build && make docker/run
```

The `entrypoint` of this project is the `run.py` file on the root path.

This project needs postgres to be successful in its operation, when running the command `make docker/run` we will start postgres database via docker-compose.

## Running Migrations

### Generating migrations

```
make docker/migrations/generate
```

### Applying changes on the database

```
make docker/migrations/upgrade
```

*If you want to know more about migrations, please read the [alembic](https://alembic.sqlalchemy.org/en/latest/) docs.*

### How to lint

`make docker/lint` to lint

`make docker/lint/fix` to lint fix

`make docker/bandit` to execute the bandit check

**Helpful commands**

_Please, check all available commands in the [Makefile](Makefile) for more information_.

## Extras infos

- If you use the [vscode](https://code.visualstudio.com/) editor we have some examples of [launch.json](.docs/vscode.md) to speed up your tests.

    *Note: When you run the install command (using docker or locally), a .env file will be created automatically based on [env.template](env.template)*
