import unittest

from pydantic import parse_obj_as, HttpUrl

from domain.health_check import HealthCheck
from domain.website import Website
from domain.website_status import WebsiteStatus


class TestHealthCheck(unittest.TestCase):

    def test_health_check(self):
        website = Website(url=parse_obj_as(HttpUrl, "http://google.com"))
        hc = HealthCheck(website=website, status=WebsiteStatus.up)
        self.assertIsNotNone(hc.status_dt)