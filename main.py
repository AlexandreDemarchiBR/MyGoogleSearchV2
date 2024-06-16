from Client import Client

client = Client()
client.search_expression("Programação")

'''
import rpyc

IP, PORT = rpyc.discover("NAIVEDB")[0]
conn = rpyc.connect(IP, PORT)
print(conn.root.search_expression("Confira"))'''