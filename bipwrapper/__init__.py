from requests.auth import HTTPBasicAuth

from bipwrapper.environment import get_environment
from bipwrapper.service.group import Group
from bipwrapper.service.multi import Multi
from bipwrapper.service.single import Single
from bipwrapper.service.upload import Upload


class BipWrapper:
    def __init__(self, env, uname, passwd):
        environment = get_environment(env)
        auth = HTTPBasicAuth(uname, passwd)
        self.all = Group(environment.single_url, auth)
        self.single = Single(environment.single_url, auth)
        self.multi = Multi(environment.multi_url, auth)
        self.upload = Upload(auth)


__version__ = "1.3.0"
