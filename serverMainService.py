from MainService import MainService

PORT = 18861

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MainService, port=PORT, auto_register=True)
    print("Listening on port", PORT)
    t.start()