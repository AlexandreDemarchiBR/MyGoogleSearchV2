import rpyc


class ReadService(rpyc.Service):
    ALIASES = ['READSERVICE']
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass
    
    def exposed_search_file(self, file_name, expression):
        # temporariamente fixo. Posteriormente será dado pelo loadbalancer
        conn = rpyc.connect('localhost', 18862)
        return conn.root.search_file(file_name, expression)