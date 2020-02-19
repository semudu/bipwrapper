from enum import Enum


class MessageType(Enum):
    TEXT = 0
    IMAGE = 2
    AUDIO = 3
    VIDEO = 4
    STICKER = 5
    CAPS = 6
    LOCATION = 7
    LINE = 9
    CONTACT = 10
    MEDIA = 13
    DOCUMENT = 14


class AddressType(Enum):
    HASH = 0
    ALL_MEMBERS = 1
    MSISDN = 2


class ButtonType(Enum):
    POST_BACK = 1
    VOICE_CALL = 2
    QR_CODE = 3
    BIP_VOICE_CALL = 4
    BIP_VIDEO_CALL = 5


class MediaMessageType(Enum):
    SINGLE = 0
    MULTIPLE = 1
    POLL = 2
    QUICK_REPLY = 3
    ORDERED = 4


class PollType(Enum):
    SINGLE_CHOOSE = 0
    MULTIPLE_CHOOSE = 1


class CType:
    BUZZ = "buzz"
    POLL = "poll"
    POSTBACK = "postback"
