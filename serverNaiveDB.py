from NaiveDB import NaiveDBService

PORT = 18862

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(NaiveDBService, port=PORT, auto_register=True)
    print("Listening on port", PORT)
    t.start()