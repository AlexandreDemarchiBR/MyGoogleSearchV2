import rpyc

class MainService(rpyc.Service):
    ALIASES = ['MAINSERVICE']

    def __init__(self):
        self.writeservice = rpyc.discover('WRITESERVICE')[0]
    
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    ''' somente um proxy para o loadbalancer
    def exposed_get_server(self):
        IP, PORT = rpyc.discover("LOADBALANCER")[0]
        conn = rpyc.connect(IP, PORT)
        return conn.root.get_server()'''
    
    # encaminha arquivo para o servidor de escrita
    def exposed_forward_upload_file(self, file_name, chunk):
        IP, PORT = self.writeservice
        conn = rpyc.connect(IP,PORT)
        conn.root.spread_upload_file(file_name, chunk)