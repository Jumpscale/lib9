from js9 import j

JSConfigBase = j.tools.configmanager.base_class_configs

from .VirtualboxClient import VirtualboxClient

class VirtualboxFactory(JSConfigBase):

    def __init__(self):
        self.__jslocation__ = "j.clients.virtualbox"
        JSConfigBase.__init__(self, VirtualboxClient)

    # def get_by_params(self, instance="main"):
    #     """
    #     name of redis connection
    #     get as follows:

    #     j.clients.redis_config.get_by_params(instance='coredns', ipaddr='localhost', port=6380, password='', unixsocket='', ardb_patch=False)

    #     """
    #     data = {}
    #     data["redisconfigname"] = redisname
    #     return self.get(instance=instance, data=data)

    @property
    def client(self):
        return self.get("default",interactive=False)
        
    # def client_get(self,zerotiernetwork):
    #     return self.get("test",data={"zerotiernetwork":zerotiernetwork})


    def test(self, instance="main"):
        """
        js9 'j.clients.virtualbox.test()'
        """
    
        cl = self.client
        cl.reset_all()


        from IPython import embed;embed(colors='Linux')
