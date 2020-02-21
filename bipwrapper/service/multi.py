from bipwrapper.type.address_type import AddressType
from .base import Base


class Multi(Base):
    def __init__(self, url, auth):
        super().__init__(url, auth, AddressType.MSISDN)

    def __get_receiver_json__(self, receivers):
        result = []
        for receiver in receivers:
            json_data = {
                "type": self.address_type.value
            }
            if self.address_type == AddressType.MSISDN:
                json_data["address"] = "90" + receiver[-10:]
            elif self.address_type == AddressType.HASH:
                json_data["address"] = receiver

            result.append(json_data)

        return result

    def __get_base_json__(self, receivers):
        return {
            "txnid": str(self.__get_txnid__()),
            "receivers": self.__get_receiver_json__(receivers),
            "composition": {
                "list": []
            }
        }

    def send_quickreply_message(self, receivers: list, postback_id, buttons_tuple):
        super().send_quickreply_message(receivers, postback_id, buttons_tuple)

    def send_poll_message(self, receivers: list, poll_id, title, description, image_url, image_ratio, poll_type,
                          options_tuple,
                          button_name):
        super().send_poll_message(receivers, poll_id, title, description, image_url, image_ratio, poll_type,
                                  options_tuple,
                                  button_name)

    def send_custom_message(self, receivers: list, message_type, args_json):
        super().send_custom_message(receivers, message_type, args_json)

    def send_text_message(self, receivers: list, message):
        super().send_text_message(receivers, message)

    def send_image(self, receivers: list, image_url, image_size, ratio):
        super().send_image(receivers, image_url, image_size, ratio)

    def send_audio(self, receivers: list, audio_url, audio_size):
        super().send_audio(receivers, audio_url, audio_size)

    def send_video(self, receivers: list, video_url, video_size, ratio):
        super().send_video(receivers, video_url, video_size, ratio)

    def send_sticker(self, receivers: list, sticker_url, item_id):
        super().send_sticker(receivers, sticker_url, item_id)

    def send_caps(self, receivers: list, caps_url, item_id, size, ratio):
        super().send_caps(receivers, caps_url, item_id, ratio)

    def send_location(self, receivers: list, latitude, longitude, title, description, zoom_level):
        super().send_location(receivers, latitude, longitude, title, description, zoom_level)

    def send_line(self, receivers: list):
        super().send_line(receivers)

    def send_contact(self, receivers: list, contact_json):
        super().send_contact(receivers, contact_json)

    def send_document(self, receivers: list, filename, filepath):
        super().send_document(receivers, filename, filepath)
