import socket


class Sock:
    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def binding_port(self):
        port = 31462
        addr = ("10.134.132.190", port)
        self._sock.bind(addr)
        return port

    def listening_accepting(self):
        self._sock.listen(self.binding_port())
        while True:
            connectedSock = Sock()
            (connectedSock) = self._sock.accept()
            self.receiving_data()
            self.change_msg()
            self.sending()

    def receiving_data(self):
        try:
            msg = self._sock.recv(1024).decode()
        except ConnectionAbortedError:
            self._sock.close()
        return str(msg)

    def change_msg(self):
        new_msg = self.receiving_data()[::-1]
        return new_msg

    def sending(self):
        msg = self.change_msg()
        self._sock.sendall(msg.encode())


def main():
    sock = Sock()
    sock.binding_port()
    sock.listening_accepting()


main()
