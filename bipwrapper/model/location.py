class Location:
    def __init__(self, lat, lon, title, desc, zoomlevel):
        self.latitute = lat
        self.longtitute = lon
        self.title = title
        self.description = desc
        self.zoomlevel = zoomlevel

    def __repr__(self):
        return str(self.__dict__)
