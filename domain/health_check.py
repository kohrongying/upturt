from datetime import datetime
from pydantic import BaseModel

from domain.website import Website
from domain.website_status import WebsiteStatus


class HealthCheck(BaseModel):
    website: Website
    status: WebsiteStatus
    status_dt: datetime = datetime.now()
