import rpyc

class MainService(rpyc.Service):
    ALIASES = ['MAINSERVICE']

    def __init__(self):
        IP, PORT = rpyc.discover('WRITESERVICE')[0]
        self.write_conn = rpyc.connect(IP, PORT)
        IP, PORT = rpyc.discover('READSERVICE')[0]
        self.read_conn = rpyc.connect(IP, PORT)

    # encaminha arquivo para o servidor de escrita
    def exposed_forward_upload_file(self, file_name, chunk):
        self.write_conn.root.spread_upload_file(file_name, chunk)
    
    def exposed_search_file(self, file_name, expression):
        self.read_conn.root.spread_upload_file(file_name, expression)



    
    def on_connect(self, conn):
        pass
    def on_disconnect(self, conn):
        pass