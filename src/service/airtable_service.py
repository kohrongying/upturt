from typing import List, Dict, Optional

import pytz
from pyairtable import Table
from pyairtable.formulas import FIELD, to_airtable_value, match

from src.domain.health_check import HealthCheck
from pydantic import validate_arguments, BaseModel
import os
from datetime import datetime
from src.domain.website_status import WebsiteStatus

api_key = os.environ.get("AIRTABLE_API_KEY")
base_id = os.environ.get("AIRTABLE_BASE_ID")
status_table_name = os.environ.get("AIRTABLE_STATUS_TABLE_NAME")
status_table = Table(api_key, base_id, status_table_name)


class AirtableStatusRecord(BaseModel):
    id: str
    createdTime: str
    fields: Dict[str, str]

    def to_health_check(self):
        website_status = WebsiteStatus.up if self.fields.get('Status', False) else WebsiteStatus.down
        status_dt_str = self.fields.get('Date', '')
        utc_dt = datetime.strptime(status_dt_str, '%Y-%m-%dT%H:%M:%S.%f%z')
        local_tz = pytz.timezone('Asia/Singapore')
        local_dt = utc_dt.replace(tzinfo=pytz.utc)
        return HealthCheck(
            url=self.fields.get('Domain'),
            status=website_status,
            status_dt=local_dt.astimezone(local_tz)
        )


class AirtableService:

    @validate_arguments
    def batch_create_health_check(self, health_check_records: List[HealthCheck]) -> None:
        try:
            status_table.batch_create([hc.to_airtable_model() for hc in health_check_records])
        except Exception as e:
            print(e)

    @staticmethod
    def batch_delete(record_ids: List[str]) -> None:
        try:
            status_table.batch_delete(record_ids)
        except Exception as e:
            print(e)

    @staticmethod
    def filter_records_created_earlier_than(target_date: str) -> List[AirtableStatusRecord]:
        try:
            created_field = FIELD("Created")
            formula = f"IS_BEFORE({created_field}, {to_airtable_value(target_date)})"
            response = status_table.all(formula=formula)
            return [AirtableStatusRecord.parse_obj(r) for r in response]
        except Exception as e:
            print(e)

    def get_most_recent_status(self, domain: str) -> Optional[AirtableStatusRecord]:
        formula = match({"Domain": domain})
        max_records = 1
        sort = ["-Created"]
        records = self.filter(formula, max_records, sort)
        return records[0] if records else None

    @staticmethod
    def filter(formula: str, max_records: int, sort: List[str]) -> List[AirtableStatusRecord]:
        try:
            response = status_table.all(formula=formula, max_records=max_records, sort=sort)
            return [AirtableStatusRecord.parse_obj(r) for r in response]
        except Exception as e:
            print(e)
