from WriteService import WriteService

PORT = 18813

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(WriteService, port=PORT, auto_register=True)
    print("Listening on port", PORT)
    t.start()