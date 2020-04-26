from enum import Enum


class AddressType(int, Enum):
    HASH = 0
    ALL_MEMBERS = 1
    MSISDN = 2
