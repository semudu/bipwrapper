from requests.auth import HTTPBasicAuth

from bipwrapper.environment import get_environment
from bipwrapper.service.group import Group
from bipwrapper.service.multi import Multi
from bipwrapper.service.single import Single
from bipwrapper.service.upload import Upload


class BipWrapper:
    def __init__(self, env, username, password):
        current_env = get_environment(env)
        auth = HTTPBasicAuth(username, password)
        self.all = Group(current_env.single_url, auth)
        self.single = Single(current_env.single_url, auth)
        self.multi = Multi(current_env.multi_url, auth)
        self.upload = Upload(auth)


__version__ = "1.3.4"
