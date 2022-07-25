from src.domain.website_status import WebsiteStatus
from pydantic import HttpUrl, validate_arguments
import urllib3

http = urllib3.PoolManager()


class HealthCheckService:

    @validate_arguments
    def ping(self, url: HttpUrl) -> WebsiteStatus:
        try:
            headers = {
                'Cache-Control': 'max-age=0, must-revalidate, no-store'
            }
            r = http.request('GET', url, headers=headers)
            mapping = {
                '200': WebsiteStatus.up,
            }
            return mapping.get(str(r.status), WebsiteStatus.down)
        except Exception as e:
            print(e)
            return WebsiteStatus.down
