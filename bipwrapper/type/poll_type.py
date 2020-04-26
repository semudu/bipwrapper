from enum import Enum


class PollType(int, Enum):
    SINGLE_CHOOSE = 0
    MULTIPLE_CHOOSE = 1
