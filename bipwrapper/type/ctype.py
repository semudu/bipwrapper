from enum import Enum


class CType(str, Enum):
    BUZZ = "Buzz"
    POLL = "Poll"
    POSTBACK = "Postback"
    STICKER = "S"
    CAPS = "C"
    PHOTO = "I"
    VIDEO = "V"
    TEXT = "T"
    LOCATION = "L"
    DOCUMENT = "Document"
    CONTACT = "vcard"
