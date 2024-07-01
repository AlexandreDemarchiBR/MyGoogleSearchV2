# arquivo que usará a classe cliente
from Client import Client
import rpyc

if __name__ == "__main__":
    client = Client()
    client.upload_file("2016_pt.jsonl")
    #client.search_expression("Programação")

    '''
    IP, PORT = rpyc.discover("NAIVEDB")[0]
    conn = rpyc.connect(IP, PORT)
    print(conn.root.search_expression("Confira"))'''