ci-test:
	python -m unittest

cron-healthcheck:
	python run_healthcheck.py

cleanup:
	python remove_historical_healthcheck.py

install:
	pip install -r requirements.txt

local:
	uvicorn main:app --reload