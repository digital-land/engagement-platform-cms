# =============================
# Utils
# =============================

server::
	 python3 manage.py runserver

# compile scss

# build docker image

# =============================
# Dependencies
# =============================

init::
	python -m pip install pip-tools
	make piptools-compile
	make dependencies

piptools-compile::
	python -m piptools compile --output-file=requirements/requirements.txt requirements/requirements.in
	python -m piptools compile requirements/dev-requirements.in

dependencies::
	pip-sync requirements/requirements.txt  requirements/dev-requirements.txt

# =============================
# Linting
# =============================

lint: 
	make black ./application
	python3 -m flake8 ./application --append-config config/.flake8

black-check:
	black --check .

black:
	python3 -m black .

# =============================
# Testing
# =============================

test: test-unit test-integration test-e2e test-acceptance

test-unit:
	python -m pytest --md-report --md-report-color=never --md-report-output=unit-tests.md tests/unit

test-integration:
	python -m pytest --md-report --md-report-color=never --md-report-output=integration-tests.md tests/integration

test-e2e:
	python -m pytest --md-report --md-report-color=never --md-report-output=e2e-tests.md tests/e2e

test-acceptance:
	python -m playwright install chromium
	python -m pytest --md-report --md-report-color=never -p no:warnings tests/acceptance

# Security

#fetch data from specifications repo
SOURCE_URL=https://raw.githubusercontent.com/digital-land/


ifeq (,$(wildcard ./makerules/specification.mk))

specification::

	@mkdir -p specification/
    curl -qfsL '$(SOURCE_URL)/specification/main/specification/schema.csv' > specification/schema.csv
    
init::  specification
endif