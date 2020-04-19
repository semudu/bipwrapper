import requests
import random


class Upload:
    def __init__(self, auth):
        self.auth = auth
        self.url = "http://timsac.turkcell.com.tr/fts/rest/file/upload"

    @staticmethod
    def __get_txnid__():
        return random.randint(1000, 9999)

    def __send_file(self, file, file_type):
        resp = requests.post(self.url,
                             auth=self.auth,
                             data={'data': '{"txnid":"' + str(
                                 self.__get_txnid__()) + '","receiver": "","avatarOwner": "","isGroup": "false","isAvatar": "false","toUser": "","fileType": "' + file_type + '"}'},
                             files=[('file', file)])
        if resp.status_code != 200:
            raise Exception(resp.text)

        return resp.json()["url"]

    def image(self, image):
        return self.__send_file(image, "P")

    def document(self, document):
        return self.__send_file(document, "D")
