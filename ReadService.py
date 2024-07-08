import rpyc


class ReadService(rpyc.Service):
    ALIASES = ['READSERVICE']
    def __init__(self):
        self.load_balancer = rpyc.connect(rpyc.discover("LOADBALANCER")[0])
    
    def exposed_search_file(self, file_name, expression):
        # dado pelo loadbalancer
        server = self.load_balancer.root.get_server_for_search()
        conn = rpyc.connect(server)
        return conn.root.search_file(file_name, expression)


    def on_connect(self, conn):
        pass
    def on_disconnect(self, conn):
        pass