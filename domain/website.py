from pydantic import BaseModel, HttpUrl

from domain.health_check import HealthCheck
from domain.website_status import WebsiteStatus
from service.health_check_service import HealthCheckService


class Website(BaseModel):
    url: HttpUrl

    def get_health_check(self) -> HealthCheck:
        status: WebsiteStatus = HealthCheckService().ping(self.url)
        return HealthCheck(url=self.url, status=status)
