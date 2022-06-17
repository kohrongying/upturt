import unittest
from pydantic import ValidationError

from domain.Website import Website


class TestWebsite(unittest.TestCase):

    def test_invalid_url_should_raise_error(self):
        with self.assertRaises(ValidationError) as context:
            Website(url="http://example")


if __name__ == '__main__':
    unittest.main()
