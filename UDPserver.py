from server import Server
import socket


class UDPServer(Server):
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

    def run(self):
        print("running on port " + str(self.PORT))
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.bind((self.HOST, self.PORT))
        while True:
            msg, addr = s.recvfrom(1024)
            print("received " + msg.decode() + " on port " + str(self.PORT) + " (UDP server)")
