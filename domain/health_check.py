from datetime import datetime
from pydantic import BaseModel, HttpUrl

from domain.website_status import WebsiteStatus


class HealthCheck(BaseModel):
    url: HttpUrl
    status: WebsiteStatus
    status_dt: datetime = datetime.now()
