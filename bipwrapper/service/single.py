from bipwrapper.type.address_type import AddressType
from .base import Base


class Single(Base):
    def __init__(self, url, auth):
        super().__init__(url, auth, AddressType.MSISDN)
