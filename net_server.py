import socket


class Sock:
    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._addr = ("0.0.0.0", 31462)
        self._msg_recv = ""
        self._msg_send = ""

    def binding_port(self):
        self._sock.bind(self._addr)

    def listening_accepting(self):
        self._sock.listen(5)
        while True:
            (connectedSock, clientAddress) = self._sock.accept()
            self._msg_recv = self.receiving_data(connectedSock)
            self._msg_send = self.change_msg()
            self.sending(connectedSock)

    def receiving_data(self, connectedSock):
        try:
            msg = connectedSock.recv(1024).decode()
            return str(msg)
        except ConnectionAbortedError:
            print("connection error.")
            connectedSock.close()

    def change_msg(self):
        new_msg = str(self._msg_recv)[::-1]
        return str(new_msg)

    def sending(self, connectedSock):
        connectedSock.sendall(self._msg_send.encode())


def main():
    sock = Sock()
    sock.binding_port()
    sock.listening_accepting()


main()
