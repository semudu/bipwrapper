from enum import Enum


class MediaType(int, Enum):
    SINGLE = 0
    MULTIPLE = 1
    POLL = 2
    QUICK_REPLY = 3
    ORDERED = 4
