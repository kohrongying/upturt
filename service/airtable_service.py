from typing import List, Dict

from pyairtable import Table
from pyairtable.formulas import FIELD, EQUAL, to_airtable_value

from domain.health_check import HealthCheck
from pydantic import validate_arguments
import os

api_key = os.environ["AIRTABLE_API_KEY"]
base_id = 'apph8KjTUqc4kP4wj'
status_table_name = os.environ["AIRTABLE_STATUS_TABLE_NAME"]
status_table = Table(api_key, base_id, status_table_name)


class AirtableService:

    @validate_arguments
    def batch_create_health_check(self, health_check_records: List[HealthCheck]):
        try:
            response = status_table.batch_create([hc.to_airtable_model() for hc in health_check_records])
        except Exception as e:
            print(e)

    @staticmethod
    def batch_delete(record_ids: List[str]):
        try:
            response = status_table.batch_delete(record_ids)
        except Exception as e:
            print(e)

    @staticmethod
    def filter_records_created_earlier_than(target_date: str) -> List[Dict[str, str]]:
        try:
            created_field = FIELD("Created")
            formula = f"IS_BEFORE({created_field}, {to_airtable_value(target_date)})"
            response = status_table.all(formula=formula)
            return response
        except Exception as e:
            print(e)