from enum import Enum


class ButtonType(Enum):
    POST_BACK = 1
    VOICE_CALL = 2
    QR_CODE = 3
    BIP_VOICE_CALL = 4
    BIP_VIDEO_CALL = 5
