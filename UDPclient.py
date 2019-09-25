import socket
from lib import *

def main():
	HOST = 'localhost'
	PORT = 9001

	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	try:
		while True:
			msg = input().upper()

			send_udp(msg, clientSocket, HOST, PORT)
			response = read_udp(clientSocket)

			print(response[0])
	
	
	except socket.error:
		clientSocket.close()

	clientSocket.close()

if __name__ == "__main__":
	main()