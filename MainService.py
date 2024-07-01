import rpyc

class MainService(rpyc.Service):
    ALIASES = ['MAINSERVICE']
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
        print("exposed_forward_upload_file")
        IP, PORT = rpyc.discover('WRITESERVICE')[0]
        conn = rpyc.connect(IP,PORT)
        conn.root.spread_upload_file(file_name, chunk)