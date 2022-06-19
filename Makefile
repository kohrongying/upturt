ci-test:
	python -m unittest

cron-healthcheck:
	python run_healthcheck.py

install:
	pip install -r requirements.txt