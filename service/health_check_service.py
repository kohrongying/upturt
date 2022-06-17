from urllib3.exceptions import NewConnectionError, MaxRetryError

from domain.website_status import WebsiteStatus
from pydantic import HttpUrl, validate_arguments
import urllib3

http = urllib3.PoolManager()


class HealthCheckService:

    @validate_arguments
    def ping(self, url: HttpUrl) -> WebsiteStatus:
        try:
            r = http.request('GET', url)
            mapping = {
                '200': WebsiteStatus.up,
            }
            return mapping.get(str(r.status), WebsiteStatus.down)
        except Exception:
            return WebsiteStatus.down
