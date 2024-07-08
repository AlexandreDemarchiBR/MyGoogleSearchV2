import rpyc
from itertools import cycle

class LoadBalancerService(rpyc.Service):
    ALIASES = ['LOADBALANCER']

    def __init__(self):
        services = rpyc.list_services()
        # List comprehension que cria uma lista de hosts cujo ALIAS começa com "NAIVE"
        services_list = [rpyc.discover(i)[0] for i in services if i.startswith('NAIVE')]
        self.server_queue = cycle(services_list)
        print('Fila inicializada', services_list)

    

    # retorna DICIONARIO no formato {'host': ip, 'port': porta} ciclando entre os nós
    def exposed_get_server_for_search(self): # this is an exposed method
        ip_port = next(self.server_queue)
        print('Respondendo', ip_port)
        return ip_port

    # retornar tupla contendo nós para inserção
    # por enquanto fixo
    def exposed_get_server_for_insertion(self):
        return (('192.168.100.2', 18862),('192.168.100.3', 18862),('192.168.100.4', 18862))
    


    def on_connect(self, conn):
        pass
    def on_disconnect(self, conn):
        pass