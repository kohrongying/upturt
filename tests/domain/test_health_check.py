import unittest

from pydantic import parse_obj_as, HttpUrl

from src.domain.health_check import HealthCheck
from src.domain.website_status import WebsiteStatus


class TestHealthCheck(unittest.TestCase):

    def test_health_check(self):
        hc = HealthCheck(url=parse_obj_as(HttpUrl, "http://google.com"), status=WebsiteStatus.up)
        self.assertIsNotNone(hc.status_dt)

    def test_to_airtable_model(self):
        hc = HealthCheck(url=parse_obj_as(HttpUrl, "http://google.com"), status=WebsiteStatus.up)
        dict = hc.to_airtable_model()
        self.assertEqual(dict["Domain"], "http://google.com")
        self.assertEqual(dict["Status"], True)
