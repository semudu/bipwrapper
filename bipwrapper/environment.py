class Base:
    def __init__(self, base_url):
        self.single_url = base_url + "/sendmsgserv"
        self.multi_url = base_url + "/sendmsgservlist"
        self.multi_diff_url = base_url + "/sendmultiusermulticontent"
        

class Production(Base):
    def __init__(self):
        super().__init__("https://tims.turkcell.com.tr/tes/rest/spi")


class Test(Base):
    def __init__(self):
        super().__init__("https://prptims.turkcell.com.tr/tes/rest/spi")


def get_environment(env):
    if env == "PROD":
        return Production()
    elif env == "TEST":
        return Test()
    else:
        raise Exception("Wrong Environment. It must be PROD or TEST.")
