import rpyc
from itertools import cycle

class LoadBalancerService(rpyc.Service):
    ALIASES = ['LOADBALANCER']

    def __init__(self):
        services = rpyc.list_services()
        # Substituir NAIVE pelo prefixo dos nós a serem ciclados
        # List comprehension que cria uma lista de dicionarios contendo as chaves 'host' e 'port' de hosts cujo ALIAS começa com "NAIVE"
        services_list = [{'host': rpyc.discover(i)[0][0], 'port': rpyc.discover(i)[0][1]} for i in services if i.startswith('NAIVE')]
        self.server_queue = cycle(services_list)
        print('Fila inicializada', services_list)

    def on_connect(self, conn):
        pass


    def on_disconnect(self, conn):
        pass

    # retorna DICIONARIO no formato {'host': ip, 'port': porta} ciclando entre os nós
    def exposed_get_server_for_search(self): # this is an exposed method
        ip_port = next(self.server_queue)
        print('Respondendo', ip_port)
        return ip_port

    # retornar lista de dicionarios contendo nós para inserção
    # formato do dicionario {'host': ip, 'port': porta}
    def exposed_get_server_for_insertion(self):
        pass