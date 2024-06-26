# Queensland Vessel Traffic Service

A backend API system that is being developed for Queensland Vessel Traffic Service (QVTS) operators.

[![Python 3.12.3](https://img.shields.io/badge/python-3.12.3-blue.svg)](https://www.python.org/downloads/release/python-3123/)
[![Django 4.2.13](https://img.shields.io/badge/django-4.2.13-blue.svg)](https://www.djangoproject.com/download/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: djlint](https://img.shields.io/badge/html%20style-djlint-blue.svg)](https://www.djlint.com)

<!-- [![Build status][badge:GithubActions:CI]][GithubActions:CI] -->
<!-- [![Code Quality][badge:GithubActions:CQ]][GithubActions:CQ] -->

## Resources

### ERD

<!-- - ![ERD](./resources/db.svg) -->
<img alt="ERD" src="./resources/db.svg" width="500" height="500" />

Note: Non-code project resources are located in the `resources` directory.

## General

### Prerequisites

- Docker; if you don't have it yet, follow the [installation instructions](https://docs.docker.com/install/#supported-platforms);
- Docker Compose; refer to the official documentation for the [installation guide](https://docs.docker.com/install/#supported-platforms).
- Git, if you don't have it yet, follow the [installation instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git);
- Pre-commit; refer to the official documentation for the pre-commit

#### Pre-commit

Note: `git` is required to be installed on your local machine.

Before doing any git commit, pre-commit should be installed globally on your local machine, and then:

```bash
# install pre-commit hooks
$ pre-commit install

# run pre-commit hooks on all files
$ pre-commit run --all-files
```

### Development environment setup

#### Build the Stack

This can take a while, especially the first time you run this particular command on your development system::

```bash
# set compose file environment variable
$ export COMPOSE_FILE=docker-compose.local.yml

# build the stack
$ docker compose build

# rebuild just the a specific service
$ docker compose build <service-name>
```

#### Run the Stack

This brings up both Django and PostgreSQL. The first time it is run it might take a while to get started, but subsequent runs will occur quickly.

Open a terminal at the project root and run the following for local development::

```bash
# set compose file environment variable
$ export COMPOSE_FILE=docker-compose.local.yml

# run the stack
$ docker compose up

# run the stack in detached mode
$ docker compose up -d

# inspect the running containers
$ docker compose ps
```

The site should start and be accessible at [http://localhost:4000](http://localhost:4000) as the proxy of [http://localhost:8000](http://localhost:8000).

#### Debugging

```python
import ipdb;
ipdb.set_trace()
```

Then run it with:

```bash
# set compose file environment variable
$ export COMPOSE_FILE=docker-compose.local.yml

# run the container for debugging
$ docker compose run --rm --service-ports django
```

#### Execute Management Commands

As with any shell command that we wish to run in our container, this is done using the `docker compose -f docker-compose.local.yml run --rm` command:

```bash
# set compose file environment variable
$ export COMPOSE_FILE=docker-compose.local.yml

# migration
$ docker compose run --rm django python manage.py migrate

# create superuser
$ docker compose run --rm django python manage.py createsuperuser

# run django shell plus (django-extensions)
$ docker compose run --rm django python manage.py shell_plus
```

#### Devcontainer setup

The project comes with a `.devcontainer` folder that contains the configuration for a development container. The development container is configured to run the project with all the necessary dependencies.

To use the development container, you need to have the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension installed in VSCode.

#### Load seed data

To load seed data, run the following command:

```bash
# run bash script to load fixtures
$ ./load_fixtures.sh
```

### Environment variables

The environment variables are split into multiple files, located in the `.envs` folder. The `.envs` folder is not committed to the repository and is ignored by git.

```bash
.envs
├── .local
│   ├── .django
│   └── .postgres
└── .production
    ├── .django
    └── .postgres
```

Should you ever need to merge .envs/.production/\* in a single `.env` run the `merge_production_dotenvs_in_dotenv.py`:

```bash
# merge production envs in a single .env
$ python merge_production_dotenvs_in_dotenv.py
```

The `.env` file will then be created, with all your production envs residing beside each other.

### Code Quality

- `mypy` is used to type check Python code.
- `eslint` is used to lint JavaScript code.
- `prettier` is used to format JavaScript code.
- `ruff` is used to lint Python code.
- `djlint` is used to lint Django templates.

#### Type checks

Running type checks with mypy:

```bash
# run mypy
$ mypy qvts
```

### Linting, Formatting & Static Analysis

This project uses [Ruff](https://github.com/astral-sh/ruff) for formatting. `ruff` is an extremely fast Python linter and code formatter that will format your code in a consistent style.

#### Ruff

##### Ruff Usage

To run Ruff as a linter, try any of the following:

```bash
ruff check                          # Lint all files in the current directory (and any subdirectories).
ruff check path/to/code/            # Lint all files in `/path/to/code` (and any subdirectories).
ruff check path/to/code/*.py        # Lint all `.py` files in `/path/to/code`.
ruff check path/to/code/to/file.py  # Lint `file.py`.

Or, to run Ruff as a formatter:

ruff format                          # Format all files in the current directory (and any subdirectories).
ruff format path/to/code/            # Format all files in `/path/to/code` (and any subdirectories).
ruff format path/to/code/*.py        # Format all `.py` files in `/path/to/code`.
ruff format path/to/code/to/file.py  # Format `file.py`.
```

Configuration for `ruff` is stored in `pyproject.toml`.

#### Djlint

##### Djlint Usage

```bash
# Lint the project
$ djlint . --lint

# Check format
$ djlint . --check

# Fix and reformat
$ djlint . --reformat
```

Configuration for `djlint` is stored in `pyproject.toml`.

#### VSCode

`.vscode/settings.json` is added to the project to enforce the above settings in VSCode. Other IDE users should configure their IDE to follow the configurations.

Certain extensions are expected to be installed in VSCode. The list of extensions can be found in `.vscode/extensions.json`.

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```bash
# set compose file environment variable
$ export COMPOSE_FILE=docker-compose.local.yml

# to run the tests
$ docker compose run --rm django coverage run -m pytest

# to run the tests (inside devcontainer)
$ coverage run -m pytest

# to report on the results (inside devcontainer)
$ coverage report

# to generate an HTML coverage report (inside devcontainer)
$ coverage html
$ open htmlcov/index.html

# to erase all the coverage data (inside devcontainer)
$ coverage erase
```

Note: prepend the commands with `docker compose -f docker-compose.local.yml run --rm django` if running outside of the container.

#### Running tests with pytest

```bash
# Running tests with pytest with verbose output (inside devcontainer)
$ pytest -rP

# if running outside of the container
# set compose file environment variable
$ export COMPOSE_FILE=docker-compose.local.yml
$ docker compose run --rm django pytest -rP
```

### Live reloading and Sass CSS compilation

#### Webpack

Webpack as front-end pipeline, the project comes configured with [Sass](https://sass-lang.com/) compilation and [live reloading](https://browsersync.io). As you change your Sass/JS source files, the task runner will automatically rebuild the corresponding CSS and JS assets and reload them in your browser without refreshing the page.

The stack comes with a dedicated node service to build the static assets, watch for changes and proxy requests to the Django app with live reloading scripts injected in the response. For everything to work smoothly, you need to access the application at the port served by the node service, which is [http://localhost:4000](http://localhost:4000) by default.

### Email Server (Development only)

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [Mailpit](https://github.com/axllent/mailpit) with a web interface is available as docker container.

Container mailpit will start automatically when you will run all docker containers.

With Mailpit running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

## Deployment

```bash
# set compose file environment variable
$ export COMPOSE_FILE=docker-compose.production.yml

# build the stack first
$ docker compose build

# run the stack
$ docker compose up

# or run the stack and detach the containers
$ docker compose up -d

# To run a migration, open up a second terminal and run:
$ docker compose run --rm django python manage.py migrate

# To create a superuser, run:
$ docker compose run --rm django python manage.py createsuperuser

# To run a shell, run:
$ docker compose run --rm django python manage.py shell

# To check the logs out, run:
$ docker compose logs

# To scale your application, run:
# Warning: don’t try to scale postgres.
$ docker compose up --scale django=4

# To see how your containers are doing run:
$ docker compose ps
```

To merge `.envs/.production/*` in a single `.env` (if required):

```bash
# merge production envs in a single `.env`
$ python merge_production_dotenvs_in_dotenv.py
```

### Postgresql database backup and restore

View backups by running the following command:

```bash
# set compose file environment variable
$ export COMPOSE_FILE=docker-compose.production.yml

# view backups:
$ docker compose run --rm postgres backups

# Create a database backup: (note: the backup will be stored in the `BACKUP_DIR_PATH` directory)
$ docker compose run --rm postgres backup

# Restore a database backup: (note: ensure all connections to the database are closed before restoring)
$ docker compose run --rm postgres restore <backup-file-name>

# Remove a database backup:
$ docker compose run --rm postgres rmbackup <backup-file-name>
```

#### Backup to Amazon S3

Use the aws cli container to upload and download backups to and from Amazon S3.
Use the following commands to upload and download backups to and from Amazon S3.
The upload command uploads the postgres `/backups` directory recursively, and the download command downloads a specific backup.

```bash
# set compose file environment variable
$ export COMPOSE_FILE=docker-compose.production.yml

# upload a backup to S3
$ docker compose run --rm awscli upload

# download a backup from S3
$ docker compose run --rm awscli download <backup_filename>.sql.gz
```

### Documentation

This project uses Sphinx documentation generator.

Build and serve HTML documentation by running the following command:

```bash
# run docs service
$ docker compose -f docker-compose.docs.yml up

# To run the docs with local services:
$ docker compose -f docker-compose.local.yml -f docker-compose.docs.yml up
```

Navigate to port `9000` to see the documentation.

Note: the `docs` service sets up a temporary SQLite file by setting the environment variable `DATABASE_URL=sqlite:///readthedocs.db` in `docs/conf.py` to avoid a dependency on PostgreSQL.

#### Inline comments

Inline comments are encouraged for documenting code that is not self-explanatory especially in the case of complex logic and design decisions. Explicit is better than implicit.

Comments should always be updated or removed when the code they refer to is changed.

#### Docstrings

Docstrings will be used to autogenerate documentation for the project and they are for documenting classes, functions, methods and modules.

<!-- The project uses [Google style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). -->

#### Generate API documentation

Edit the `docs` files and project application docstrings to create your documentation.

Sphinx can automatically include class and function signatures and docstrings in generated documentation.

## CI workflow

GitHub Actions is used for CI. The workflow is defined in `.github/workflows/ci.yml`.

The workflow is triggered on:

- every push to the `main` and `dev` branch.
- every pull request to the `main` and `dev` branch.
- manually by clicking the `Run workflow` button on the Actions page.

### Branching strategy

- `main` branch --> production branch
- `dev` branch --> development branch

All feature branches are branched from `dev` and merged back to `dev` when ready. All pull requests are made to `dev` branch.

#### Branch naming convention

Branches are named as follows: `<label>/<issue-number-if-any>-<short-description>`

Labels are as follows:

- `build`: Changes that affect the build system or external dependencies (example scopes: webpack, npm)
- `chore`: Updating libraries, copyrights or other repo setting, includes updating dependencies.
- `ci`: Changes to our CI configuration files and scripts (example scopes: GitHub Actions)
- `docs`: Non-code changes, such as fixing typos or adding new documentation
- `feat`: a commit of the type feat introduces a new feature to the codebase
- `fix`: A commit of the type fix patches a bug in your codebase
- `perf`: A code change that improves performance
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `test`: Adding missing tests or correcting existing tests
- `ui`: Updating the UI (small changes) and style files
- `misc`: Miscellaneous changes that do not fit any of the above scopes

Example:

- Feature branch for issue #112 - `feat/112-add-login-page`
- Bugfix branch for issue #113 - `fix/113-fix-login-redirection-error-page`

Working on same feature as someone else? No problem. First, branch out from the feature branch. Then, name your branch as follows: `feat/<issue-number-if-any>-<feature-short-description>/<your-initials>`. e.g. `feat/112-add-login-page/ns`.

### Commit message convention

**Avoid using single line commit messages.**

The commit message template is provided in `.gitmessage` file. To use it, run the following command:

```bash
# set commit message template
$ git config commit.template .gitmessage
```

All commit messages should follow the following convention as described in the template:

```bash
Title
# No more than 50 chars. #### 50 chars is here:  #

Body: Explain *what* and *why* (not *how*). Include issue number if any.
# Wrap at 72 chars. ################################## which is here:  #

```

Try to include [good commit log messages](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

## Bug Reports

Please use the GitHub issue tracker to report any bugs. Follow the template provided.

## Pull Requests

Follow the template provided. All pull requests should be made to the `dev` branch.

## External References

- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Sphinx](https://www.sphinx-doc.org/en/master/)
- [Ruff](https://docs.astral.sh/ruff/)

<!-- [GithubActions:CI]: https://github.com/nixsiow/qvts/actions?query=workflow%3A%22Run+CI%22 -->
<!-- [badge:GithubActions:CI]: https://github.com/nixsiow/qvts/workflows/Run%20CI/badge.svg -->
<!-- [GithubActions:CQ]: https://github.com/nixsiow/qvts/actions?query=workflow%3A%22Code+quality+checks%22 -->
<!-- [badge:GithubActions:CQ]: https://github.com/nixsiow/qvts/workflows/Code%20quality%20checks/badge.svg -->
