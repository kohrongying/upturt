from service.airtable_service import AirtableService
from service.utils import get_datetime_n_days_ago

if __name__ == '__main__':
    datetime_two_weeks_ago: str = get_datetime_n_days_ago(14)
    records = AirtableService.filter_records_created_earlier_than(datetime_two_weeks_ago)
    record_ids = [record.get("id") for record in records]
    AirtableService.batch_delete(record_ids)
    print(f"Deleted {len(record_ids)} records before {datetime_two_weeks_ago}")
