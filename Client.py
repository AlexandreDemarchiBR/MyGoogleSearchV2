import rpyc
import os

class Client():
    def __init__(self):
        IP, PORT = rpyc.discover("MAINSERVICE")[0]
        self.conn = rpyc.connect(IP, PORT)


    # Faz upload de arquivo, dividindo em chunks
    def upload_file(self, file_path, chunk_size=1024*1024):
        file_name = os.path.basename(file_path)
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                self.conn.root.forward_upload_file(file_name, chunk)


    def search_expression(self, file_name, expression):
        return self.conn.forward_search_expression(file_name, expression)
