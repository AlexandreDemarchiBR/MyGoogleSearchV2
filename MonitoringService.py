import rpyc

class MonitoringService(rpyc.Service):
    ALIASES = ['MONITORINGSERVICE']
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_register_status(self):
        return 42