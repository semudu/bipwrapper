from bipwrapper.type.ctype import CType
from .document import Document
from .location import Location
from .poll import Poll
from .postback import Postback
from .vcard import VCard


class Request:
    def __init__(self, request):
        self.sender = request["sender"]
        self.type = request["type"]
        self.msgid = request["msgid"]
        self.sendtime = request["sendtime"]
        self.txnid = request["txnid"]
        self.avatar_url = request["avatarUrl"] if "avatarUrl" in request else None 
        self.nickname = request["nickname"] if "nickname" in request else None
        self.ctype = CType(request["ctype"])

        if self.ctype in (CType.TEXT, CType.CAPS, CType.STICKER, CType.PHOTO, CType.LOCATION):
            self.content = request["content"]

        if self.ctype == CType.CONTACT:
            self.vcard = VCard(request["vcard"]["value"])

        if self.ctype == CType.DOCUMENT:
            doc = request["document"]
            self.document = Document(doc["filepath"], doc["filepath"], doc["extension"], doc["size"])

        if self.ctype == CType.LOCATION:
            loc = request["location"]
            self.location = Location(loc["lat"], loc["lon"], loc["title"], loc["desc"], loc["zoomlevel"])

        if self.ctype == CType.POLL:
            poll = request["poll"]
            self.poll = Poll(poll["pollid"], poll["optionids"])

        if self.ctype == CType.POSTBACK:
            postback = request["postback"]
            self.postback = Postback(postback["postbackid"], postback["payload"])

    def __repr__(self):
        return str(self.__dict__)
