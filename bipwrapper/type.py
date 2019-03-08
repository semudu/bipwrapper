from enum import Enum


class MessageType(Enum):
    TEXT = "0"
    IMAGE = "2"
    AUDIO = "3"
    VIDEO = "4"
    STICKER = "5"
    CAPS = "6"
    LOCATION = "7"
    LINE = "9"
    CONTACT = "10"
    TEMPLATE = "13"
    DOCUMENT = "14"
