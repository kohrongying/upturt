import unittest

from pydantic import ValidationError, HttpUrl, parse_obj_as

from domain.website_status import WebsiteStatus
from service.airtable_service import AirtableStatusRecord
from service.health_check_service import HealthCheckService


class TestAirtableService(unittest.TestCase):

    def test_airtable_status_record_model(self):
        airtable_response = {'id': 'recJ5MjtVZL0X7b2l', 'createdTime': '2022-06-19T08:39:25.000Z', 'fields': {'Domain': 'https://rongying.co', 'Date': '2022-06-19T08:39:20.254Z', 'Created': '2022-06-19T08:39:25.000Z'}}
        r = AirtableStatusRecord.parse_obj(airtable_response)
        self.assertEqual(r.id, 'recJ5MjtVZL0X7b2l')
        self.assertEqual(r.createdTime, '2022-06-19T08:39:25.000Z')
        self.assertEqual(r.fields, {'Domain': 'https://rongying.co', 'Date': '2022-06-19T08:39:20.254Z', 'Created': '2022-06-19T08:39:25.000Z'})
