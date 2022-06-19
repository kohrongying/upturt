from typing import List
from domain.health_check import HealthCheck
from domain.website import Website
from repository.website_repository import WebsiteRepository
from service.airtable_service import AirtableService, AirtableStatusRecord


class UiService:

    @staticmethod
    def get_most_recent_records() -> List[HealthCheck]:
        websites: List[Website] = WebsiteRepository().websites
        health_check_records: List[HealthCheck] = []
        for website in websites:
            airtable_records: List[AirtableStatusRecord] = AirtableService().get_most_recent_status(website.url)
            if len(airtable_records) > 0:
                health_check_records.append(airtable_records[0].to_health_check())

        return health_check_records
