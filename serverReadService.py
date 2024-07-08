from ReadService import ReadService

PORT = 18814

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(ReadService, port=PORT, auto_register=True)
    print("Listening on port", PORT)
    t.start()