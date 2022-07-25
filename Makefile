test:
	python -m unittest

cron-healthcheck:
	python -m src.cron.run_healthcheck

cleanup:
	python -m src.cron.run_cleanup

install:
	pip install -r requirements.txt

local:
	source .env-dev && uvicorn main:app --reload