import rpyc

class WriteService(rpyc.Service):
    ALIASES = ['WRITESERVICE']
    def __init__(self):
        IP, PORT = rpyc.discover("LOADBALANCER")[0]
        self.load_balancer = rpyc.connect(IP, PORT)
    
    def exposed_spread_upload_file(self, file_name, chunk):     
        nodes = self.load_balancer.root.get_server_for_insertion()
        conn1 = rpyc.connect(nodes[0][0], nodes[0][1])
        conn2 = rpyc.connect(nodes[1][0], nodes[1][1])
        conn3 = rpyc.connect(nodes[2][0], nodes[2][1])
        connections = [conn1, conn2, conn3]
        for conn in connections:
            conn.root.persist_file(file_name, chunk)


    def on_connect(self, conn):
        pass
    def on_disconnect(self, conn):
        pass