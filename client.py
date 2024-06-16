import rpyc


IP, PORT = rpyc.discover("NAIVEDB")[0]
conn = rpyc.connect(IP, PORT)
print(conn.root.search_expression("Confira"))