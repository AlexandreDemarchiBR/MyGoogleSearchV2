import rpyc

class DispatcherService(rpyc.Service):
    ALIASES = ['DISPATCHER']
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    # somente um proxy para o loadbalancer
    def exposed_get_server(self):
        IP, PORT = rpyc.discover("LOADBALANCER")[0]
        conn = rpyc.connect(IP, PORT)
        return conn.root.get_server()
    
    # propaga arquivo enviado pelo cliente para todos os nós disponiveis
    def exposed_spread_upload_file(self, file_name, chunk):
        services = rpyc.list_services()
        # List comprehension que cria uma lista de dicionarios contendo as chaves 'host' e 'port' de hosts cujo ALIAS começa com "NAIVE"
        services_list = [{'host': rpyc.discover(i)[0][0], 'port': rpyc.discover(i)[0][1]} for i in services if i.startswith('NAIVE')]
        for node in services_list:
            conn = rpyc.connect(node['host'], node['port'])
            with open(file_name, 'ab') as f:
                f.write(chunk)
