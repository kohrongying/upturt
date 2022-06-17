from pathlib import Path
from typing import List

from pydantic import BaseModel, HttpUrl, parse_obj_as

from service.utils import get_project_root


class WebsiteRepository(BaseModel):
    website_filename: str = ".websites"
    website_folder_dir: Path = get_project_root()
    websites: List[HttpUrl] = []

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.import_from_file()

    def import_from_file(self):
        website_filepath = self.website_folder_dir / self.website_filename
        with open(website_filepath) as f:
            self.websites = [parse_obj_as(HttpUrl, line.rstrip()) for line in f]
