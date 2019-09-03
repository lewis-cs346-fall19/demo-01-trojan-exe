import socket

class Sock:
    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._addr = ("localhost", 31462)

    def binding_port(self):
        self._sock.bind(self._addr)

    def listening_accepting(self):
        self._sock.listen(5)
        while True:
            (connectedSock, clientAddress) = self._sock.accept()
            self.receiving_data(connectedSock, clientAddress)
            self.change_msg()
            self.sending(connectedSock)

    def receiving_data(self, connectedSock):
        try:
            msg = connectedSock.recv(1024).decode()
        except ConnectionAbortedError:
            print("connection error.")
            connectedSock.close()
        return str(msg)

    def change_msg(self):
        new_msg = self.receiving_data()[::-1]
        return new_msg

    def sending(self,connectedSock):
        msg = self.change_msg()
        connectedSock.sendall(msg.encode())


def main():
    sock = Sock()
    sock.binding_port()
    sock.listening_accepting()


main()
