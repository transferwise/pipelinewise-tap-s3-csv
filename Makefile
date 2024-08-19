venv:
	python3 -m venv venv ;\
	. ./venv/bin/activate ;\
	pip install --upgrade pip setuptools wheel;\
	pip install -e .[test]

pylint:
	. ./venv/bin/activate ;\
	pylint --rcfile .pylintrc tap_s3_csv/

unit_tests:
	. ./venv/bin/activate ;\
	pytest tests/unit --cov=tap_s3_csv --cov-fail-under=30

integration_tests:
	. ./venv/bin/activate ;\
	pytest tests/integration --cov=tap_s3_csv --cov-fail-under=84
