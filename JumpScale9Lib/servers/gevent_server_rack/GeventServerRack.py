
from js9 import j

JSBASE = j.application.jsbase_get_class()

class GeventServerRack(JSBASE):

    def __init__(self):
        JSBASE.__init__(self)
        self.servers = []

    def add(self,server):
        self.servers.append(server)

    def start(self):
        started = []
        try:
            for server in self.servers[:]:
                server.start()
                started.append(server)
                name = getattr(server, 'name', None) or server.__class__.__name__ or 'Server'
                self.logger.info('%s started on %s', name, server.address)
        except:
            self.stop(started)
            raise

    def stop(self, servers=None):
        if servers is None:
            servers = self.servers[:]
        for server in servers:
            try:
                server.stop()
            except:
                if hasattr(server, 'loop'): # gevent >= 1.0
                    server.loop.handle_error(server.stop, *sys.exc_info())
                else: # gevent <= 0.13
                    import traceback
                    traceback.print_exc()
