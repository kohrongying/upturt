import unittest

from pydantic import ValidationError, HttpUrl, parse_obj_as

from src.domain.website_status import WebsiteStatus
from src.service.health_check_service import HealthCheckService


class TestHealthCheckService(unittest.TestCase):
    health_check_service = HealthCheckService()

    def test_ping_should_return_up(self):
        result = self.health_check_service.ping(parse_obj_as(HttpUrl, "https://www.google.com"))
        self.assertEqual(result, WebsiteStatus.up)

    def test_ping_with_invalid_url_should_raise_error(self):
        with self.assertRaises(ValidationError) as context:
            self.health_check_service.ping("http://www")

