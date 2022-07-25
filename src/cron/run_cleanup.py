import math
from typing import List

from src.domain.website import Website
from src.repository.website_repository import WebsiteRepository
from src.service.airtable_service import AirtableStatusRecord, AirtableService
from src.service.utils import get_datetime_n_days_ago


def calculate_max_data_storage_days() -> int:
    websites: List[Website] = WebsiteRepository().websites
    airtable_limit = 1200
    data_points_per_site_daily = 24 / 2
    num_days: int = math.floor(airtable_limit / (len(websites) * data_points_per_site_daily))
    return int(num_days)


if __name__ == '__main__':
    nmax_days_for_data_storage = calculate_max_data_storage_days()
    datetime_limit: str = get_datetime_n_days_ago(nmax_days_for_data_storage)

    records: List[AirtableStatusRecord] = AirtableService.filter_records_created_earlier_than(datetime_limit)
    record_ids: List[str] = [record.id for record in records]

    AirtableService.batch_delete(record_ids)
    print(f"Deleted {len(record_ids)} records before {datetime_limit} ({nmax_days_for_data_storage} days ago)")
