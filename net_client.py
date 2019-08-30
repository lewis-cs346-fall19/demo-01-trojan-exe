import socket


class Client:

    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connection(self):
        host = "localhost"
        addr = (host, 31462)
        self._sock.connect(addr)

    def generating_data(self):
        for i in range(10):
            msg = "this is message " + str(i)
            self._sock.sendall(msg.encode())
            get = self._sock.recv(1024)
            print(get)


def main():
    client = Client()
    client.connection()
    client.generating_data()


main()
