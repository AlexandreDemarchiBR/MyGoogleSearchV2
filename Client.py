import rpyc
import os

class Client():
    def __init__(self):
        IP, PORT = rpyc.discover("MAIN")[0]
        self.disp_conn = rpyc.connect(IP, PORT)
        print("MAIN: IP {IP}, PORT {PORT}")

    # Faz upload de arquivo, dividindo em chunks
    def upload_file(self, file_path, chunk_size=1024*1024):
        file_name = os.path.basename(file_path)
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                self.disp_conn.root.forward_upload_file(file_name, chunk)

    """# pede um nó para o Main, se conecta ao nó e realiza a pesquisa nele
    def search_expression(self, expression: str):
        node = self.disp_conn.root.get_server()
        HOST = node['host']
        PORT = node['port']
        conn = rpyc.connect(HOST, PORT)
        print("NODE: IP {HOST}, PORT {PORT}")
        return conn.root.search_expression(expression)
"""

