from server import Server
import socket

from lib import *


class UDPServer(Server):
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

    def run(self):
        print("running on port " + str(self.PORT))
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.bind((self.HOST, self.PORT))
        while True:
            msg = read_udp(s)
            print("received " + msg + " on port " + str(self.PORT) + " (UDP server)")

