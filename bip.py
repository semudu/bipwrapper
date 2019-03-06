from enum import Enum
import requests
import random


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
    TEMPLATE = 13
    DOCUMENT = 14


class BIP:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    @staticmethod
    def __get_txnid__():
        return random.randint(1000, 9999)

    @staticmethod
    def __get_receiver_json__(receiver):
        return {
            "type": 2,
            "address": receiver
        }

    def __send_message__(self, sender, post_json):
        # TODO
        pass

    def __get_base_json__(self, receiver, message_type):
        return {
            "txnid": self.__get_txnid__(),
            "receiver": self.__get_receiver_json__(receiver),
            "composition": {
                "list": [
                    {
                        "type": message_type
                    }
                ]
            }
        }

    def __get_post_json(self, receiver, message_type, json):
        json_data = self.__get_base_json__(receiver, message_type)
        return {**json_data, **json}

    def send_custom_message(self, sender, receiver, message_type, args_json):
        post_json = self.__get_post_json(receiver, message_type, args_json)
        self.__send_message__(sender, post_json)

    def send_text_message(self, sender, receiver, message):
        post_json = self.__get_post_json(receiver, MessageType.TEXT, {
            "message": message
        })
        self.__send_message__(sender, post_json)

    def send_image(self, sender, receiver, image_url, image_size, ratio):
        post_json = self.__get_post_json(receiver, MessageType.IMAGE, {
            "message": image_url,
            "size": image_size,
            "ratio": ratio
        })
        self.__send_message__(sender, post_json)

    def send_audio(self, sender, receiver, audio_url, audio_size):
        post_json = self.__get_post_json(receiver, MessageType.AUDIO, {
            "message": audio_url,
            "size": audio_size
        })
        self.__send_message__(sender, post_json)

    def send_video(self, sender, receiver, video_url, video_size, ratio):
        post_json = self.__get_post_json(receiver, MessageType.VIDEO, {
            "message": video_url,
            "size": video_size,
            "ratio": ratio
        })
        self.__send_message__(sender, post_json)

    def send_sticker(self, sender, receiver, sticker_url, item_id):
        post_json = self.__get_post_json(receiver, MessageType.STICKER, {
            "message": sticker_url,
            "itemid": item_id
        })
        self.__send_message__(sender, post_json)

    def send_caps(self, sender, receiver, caps_url, item_id, size, ratio):
        post_json = self.__get_post_json(receiver, MessageType.CAPS, {
            "message": caps_url,
            "itemid": item_id,
            "ratio": ratio,
            "size": size
        })
        self.__send_message__(sender, post_json)

    def send_location(self, sender, receiver, latitude, longitude, title, description, zoom_level):
        post_json = self.__get_post_json(receiver, MessageType.LOCATION, {
            "location": {
                "lat": latitude,
                "lon": longitude,
                "title": title,
                "desc": description,
                "zoomlevel": zoom_level
            }
        })
        self.__send_message__(sender, post_json)

    def send_line(self, sender, receiver):
        post_json = self.__get_base_json__(receiver, MessageType.LINE)
        self.__send_message__(sender, post_json)

    # contact_json example
    #
    # {
    #     "name": "Cemal",
    #     "surname": "Önder",
    #     "phonenumbers": ["905332108323", "905XXXXXXXXX"],
    #     "addresses": [{
    #         "address": "Bahçelievler, Yenibosna, Atatürk Caddesi",
    #         "postalcode": "34197",
    #         "city": "İstanbul",
    #         "country": "Türkiye"
    #     }]
    # }
    def send_contact(self, sender, receiver, contact_json):
        self.send_custom_message(sender, receiver, MessageType.CONTACT, contact_json)

    def send_document(self, sender, receiver, filename, filepath):
        post_json = self.__get_post_json(receiver, MessageType.DOCUMENT, {
            "document": {
                "filename": filename,
                "filepath": filepath
            }
        })
        self.__send_message__(sender, post_json)
