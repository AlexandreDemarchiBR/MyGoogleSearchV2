import rpyc

class WriteService(rpyc.Service):
    ALIASES = ['WRITESERVICE']
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass
    
    def exposed_spread_upload_file(self, file_name, chunk):
        # temporariamente fixo. Posteriormente será dado pelo loadbalancer
        #conn = rpyc.connect('localhost', 18862)
        
        # temporariamente fixo, mas para maquinas virtuais: alpha, bravo, charlie
        nodes = [('192.168.100.2', 18862),('192.168.100.3', 18862),('192.168.100.4', 18862)]
        conn1 = rpyc.connect(nodes[0][0], nodes[0][1])
        conn2 = rpyc.connect(nodes[1][0], nodes[1][1])
        conn3 = rpyc.connect(nodes[2][0], nodes[2][1])
        connections =  [conn1, conn2, conn3]
        for conn in connections:
            conn.root.persist_file(file_name, chunk)