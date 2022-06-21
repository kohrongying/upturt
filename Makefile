ci-test:
	python -m unittest

cron-healthcheck:
	python run_healthcheck.py

cleanup:
	python run_cleanup.py

install:
	pip install -r requirements.txt

local:
	uvicorn main:app --reload