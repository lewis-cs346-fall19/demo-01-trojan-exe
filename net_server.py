import socket


# Author: Ian Fang, Chaoneng Quan.

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
        (connectedSock, clientAddress) = self._sock.accept()
        while True:
            self._msg_recv = self.receiving_data(connectedSock)
            if not self._msg_recv:
                print("Connection Error")
                connectedSock.close()
                break
            self._msg_send = self.change_msg()
            self.sending(connectedSock)

    def receiving_data(self, connectedSock):
        msg = connectedSock.recv(1024).decode()
        return str(msg)

    def change_msg(self):
        new_msg = "Message from server: " + str(self._msg_recv)[::-1]
        return str(new_msg)

    def sending(self, connectedSock):
        connectedSock.sendall(self._msg_send.encode())


def main():
    sock = Sock()
    sock.binding_port()
    sock.listening_accepting()


main()
