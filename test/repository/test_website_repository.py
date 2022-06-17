from pathlib import Path
from unittest import TestCase

from pydantic import parse_obj_as, HttpUrl

from repository.website_repository import WebsiteRepository


class TestWebsiteRepository(TestCase):
    def test_import_from_empty_file_should_return_empty_list(self):
        repo = WebsiteRepository(
            website_folder_dir=Path(__file__).parent,
            website_filename=".websites_empty",
        )
        self.assertEqual(repo.website_filename, ".websites_empty")
        self.assertEqual(len(repo.websites), 0)

    def test_import_from_file_should_return_list(self):
        repo = WebsiteRepository(website_folder_dir=Path(__file__).parent)
        self.assertEqual(repo.websites, [parse_obj_as(HttpUrl, "http://example.com"), parse_obj_as(HttpUrl, "http://test.com")])
