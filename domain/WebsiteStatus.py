from enum import Enum


class WebsiteStatus(str, Enum):
    up = 'up'
    down = 'down'
