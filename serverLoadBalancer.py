from LoadBalancer import LoadBalancerService

PORT = 18812

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(LoadBalancerService, port=PORT, auto_register=True)
    print("Listening on port", PORT)
    t.start()