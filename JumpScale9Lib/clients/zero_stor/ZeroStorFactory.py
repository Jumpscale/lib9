from .ZeroStorClient import ZeroStorClient
from js9 import j


class ZeroStorFactory:

    def __init__(self):
        self.__jslocation__ = "j.clients.zerostor"
        self.__imports__ = "requests"
        self.logger = j.logger.get("j.clients.zerostor")

    def getClient(self, ...):
        """
        # Getting client via accesstoken


        """
        return ZeroStorClient...)