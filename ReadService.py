import rpyc


class ReadService(rpyc.Service):
    ALIASES = ['READSERVICE']
    def __init__(self):
        IP, PORT = rpyc.discover("LOADBALANCER")[0]
        self.load_balancer = rpyc.connect(IP, PORT)
    
    def exposed_search_file(self, file_name, expression):
        # dado pelo loadbalancer
        IP, PORT = self.load_balancer.root.get_server_for_search()
        conn = rpyc.connect(IP, PORT)
        return conn.root.search_file(file_name, expression)


    def on_connect(self, conn):
        pass
    def on_disconnect(self, conn):
        pass