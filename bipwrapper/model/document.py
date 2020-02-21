class Document:
    def __init__(self, filename, filepath, extension, size):
        self.filename = filename
        self.filepath = filepath
        self.extension = extension
        self.size = size

    def __repr__(self):
        return str(self.__dict__)
