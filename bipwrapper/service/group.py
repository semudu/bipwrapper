from bipwrapper.type.address_type import AddressType
from .base import Base


class Group(Base):
    def __init__(self, url, auth):
        super().__init__(url, auth, AddressType.ALL_MEMBERS)

    def send_quickreply_message(self, postback_id, buttons_tuple):
        super().send_quickreply_message(None, postback_id, buttons_tuple)

    def send_poll_message(self, poll_id, title, description, image_url, image_ratio, poll_type, options_tuple,
                          button_name):
        super().send_poll_message(None, poll_id, title, description, image_url, image_ratio, poll_type, options_tuple,
                                  button_name)

    def send_custom_message(self, message_type, args_json):
        super().send_custom_message(None, message_type, args_json)

    def send_text_message(self, message):
        super().send_text_message(None, message)

    def send_image(self, image_url, image_size, ratio):
        super().send_image(None, image_url, image_size, ratio)

    def send_audio(self, audio_url, audio_size):
        super().send_audio(None, audio_url, audio_size)

    def send_video(self, video_url, video_size, ratio):
        super().send_video(None, video_url, video_size, ratio)

    def send_sticker(self, sticker_url, item_id):
        super().send_sticker(None, sticker_url, item_id)

    def send_caps(self, caps_url, item_id, size, ratio):
        super().send_caps(None, caps_url, item_id, ratio)

    def send_location(self, latitude, longitude, title, description, zoom_level):
        super().send_location(None, latitude, longitude, title, description, zoom_level)

    def send_line(self):
        super().send_line(None)

    def send_contact(self, contact_json):
        super().send_contact(None, contact_json)

    def send_document(self, filename, filepath):
        super().send_document(None, filename, filepath)
