class VCard:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.__dict__)
