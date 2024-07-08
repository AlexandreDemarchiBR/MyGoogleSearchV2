import rpyc

class WriteService(rpyc.Service):
    ALIASES = ['WRITESERVICE']
    def __init__(self):
        self.load_balancer = rpyc.connect(rpyc.discover("LOADBALANCER")[0])
    
    def exposed_spread_upload_file(self, file_name, chunk):     
        nodes = self.load_balancer.root.get_server_for_insertion()
        conn1 = rpyc.connect(nodes[0])
        conn2 = rpyc.connect(nodes[1])
        conn3 = rpyc.connect(nodes[2])
        connections = [conn1, conn2, conn3]
        for conn in connections:
            conn.root.persist_file(file_name, chunk)


    def on_connect(self, conn):
        pass
    def on_disconnect(self, conn):
        pass