from datetime import datetime
from pydantic import BaseModel, HttpUrl

from domain.website_status import WebsiteStatus


class HealthCheck(BaseModel):
    url: HttpUrl
    status: WebsiteStatus
    status_dt: datetime = datetime.now().astimezone()

    def to_airtable_model(self):
        return {
            "Domain": self.url,
            "Status": "true" if self.status == WebsiteStatus.up else "false",
            "Date": str(self.status_dt)
        }

