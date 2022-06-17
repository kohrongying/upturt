ci-test:
	python -m unittest

cron-healthcheck:
	python main.py

install:
	pip install -r requirements.txt