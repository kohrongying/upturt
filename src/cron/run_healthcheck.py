from typing import List

from src.domain.health_check import HealthCheck
from src.domain.website import Website
from src.repository.website_repository import WebsiteRepository
from src.service.airtable_service import AirtableService

if __name__ == '__main__':
    websites: List[Website] = WebsiteRepository().websites
    health_check_records: List[HealthCheck] = [w.get_health_check() for w in websites]
    print(health_check_records)
    AirtableService().batch_create_health_check(health_check_records)


