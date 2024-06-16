import rpyc

class LoadBalancerService(rpyc.Service):
    ALIASES = ['LOADBALANCER']
    def on_connect(self, conn):
        self.services_list = rpyc.list_services()

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        pass

    def exposed_get_answer(self): # this is an exposed method
        return 42

    exposed_the_real_answer_though = 43     # an exposed attribute

    def get_question(self):  # while this method is not exposed
        return "what is the airspeed velocity of an unladen swallow?"