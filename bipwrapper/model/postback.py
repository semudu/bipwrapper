class Postback:
    def __init__(self, id, payload):
        self.id = id
        self.value = payload

    def __repr__(self):
        return str(self.__dict__)
