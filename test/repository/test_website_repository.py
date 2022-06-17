import pathlib
from unittest import TestCase

from repository.website_repository import WebsiteRepository


class TestWebsiteRepository(TestCase):
    def test_import_from_empty_file_should_return_empty_list(self):
        repo = WebsiteRepository(
            website_folder_dir=pathlib.Path().absolute(),
            website_filename=".websites_empty",
        )
        self.assertEqual(repo.websites, [])

    def test_import_from_file_should_return_list(self):
        repo = WebsiteRepository(website_folder_dir=pathlib.Path().absolute())
        self.assertEqual(repo.websites, ["http://example.com", "http://test.com"])