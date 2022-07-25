import unittest

from datetime import date
import pytz

from src.domain.website_status import WebsiteStatus
from src.service.airtable_service import AirtableStatusRecord


class TestAirtableService(unittest.TestCase):

    def test_airtable_status_record_model(self):
        airtable_response = {'id': 'recJ5MjtVZL0X7b2l', 'createdTime': '2022-06-19T08:39:25.000Z', 'fields': {'Domain': 'https://rongying.co', 'Date': '2022-06-19T08:39:20.254Z', 'Created': '2022-06-19T08:39:25.000Z'}}
        r = AirtableStatusRecord.parse_obj(airtable_response)
        self.assertEqual(r.id, 'recJ5MjtVZL0X7b2l')
        self.assertEqual(r.createdTime, '2022-06-19T08:39:25.000Z')
        self.assertEqual(r.fields, {'Domain': 'https://rongying.co', 'Date': '2022-06-19T08:39:20.254Z', 'Created': '2022-06-19T08:39:25.000Z'})

    def test_airtable_status_record_to_health_check(self):
        airtable_response = {'id': 'recJ5MjtVZL0X7b2l', 'createdTime': '2022-06-19T08:39:25.000Z',
                             'fields': {'Domain': 'https://rongying.co', 'Date': '2022-06-19T08:39:20.254Z',
                                        'Created': '2022-06-19T08:39:25.000Z'}}
        r = AirtableStatusRecord.parse_obj(airtable_response)
        hc = r.to_health_check()
        self.assertEqual(hc.url, 'https://rongying.co')
        self.assertEqual(hc.status, WebsiteStatus.down)
        local_tz = pytz.timezone('Asia/Singapore')

        self.assertEqual(hc.status_dt.date(), date(2022, 6, 19))
        self.assertEqual(hc.status_dt.hour, 16)
        self.assertEqual(hc.status_dt.minute, 39)
