import unittest
from unittest import mock

from pydantic import ValidationError, parse_obj_as, HttpUrl

from src.domain.health_check import HealthCheck
from src.domain.website import Website
from src.domain.website_status import WebsiteStatus


class TestWebsite(unittest.TestCase):

    def test_invalid_url_should_raise_error(self):
        with self.assertRaises(ValidationError) as context:
            Website(url="http://example")

    @mock.patch('src.service.health_check_service')
    def test_get_health_check(self, mock_service):
        url: HttpUrl = parse_obj_as(HttpUrl, "http://google.com")
        website = Website(url=url)
        hc = HealthCheck(url=url, status=WebsiteStatus.up)

        mock_service.ping.return_value = WebsiteStatus.up
        self.assertEqual(website.get_health_check(), hc)
