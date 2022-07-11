from typing import List
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from domain.health_check import HealthCheck
from domain.website import Website
from repository.website_repository import WebsiteRepository
from service.airtable_service import AirtableService, AirtableStatusRecord

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get('/healthcheck')
def healthcheck():
    return {'status': 'up'}


@app.get("/")
def read_root():
    websites: List[Website] = WebsiteRepository().websites
    health_check_records: List[HealthCheck] = []
    for website in websites:
        record: AirtableStatusRecord = AirtableService().get_most_recent_status(website.url)
        if record:
            health_check_records.append(record.to_health_check())
    return health_check_records
