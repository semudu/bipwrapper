from enum import Enum


class CType(Enum):
    BUZZ = "Buzz"
    POLL = "Poll"
    POSTBACK = "Postback"
    STICKER = "S"
    CAPS = "C"
    PHOTO = "I"
    TEXT = "T"
    LOCATION = "L"
    DOCUMENT = "Document"
    CONTACT = "vcard"
