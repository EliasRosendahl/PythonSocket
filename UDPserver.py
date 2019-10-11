from server import Server
import socket

from lib import *


class UDPServer(Server):
	def __init__(self, HOST, PORT):
		self.HOST = HOST
		self.PORT = PORT

	def run(self):
		print("running on port " + str(self.PORT))
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		serverSocket.bind((self.HOST, self.PORT))
		while True:
			msg, addr = read_udp(serverSocket)
			print("Received {} from {} on port {} (UDP server)".format(msg, str(addr[0]), str(addr[1])))
			
			response = ""
			if msg == "L":
				response = file_content("/proc/loadavg")	
				#response = "/proc/loadavg"
			elif msg == "U":
				response = file_content("/proc/uptime")
				#response = "/proc/uptime"
			elif msg == "X":
				response = "Terminated server..."
				send_udp(response, serverSocket, addr[0], addr[1])
				serverSocket.close()
				exit()
			else:
				response = "Unknown command..."

			send_udp(response, serverSocket, addr[0], addr[1])