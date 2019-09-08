import socket


def main():
    HOST = 'localhost'
    PORT = 9001

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        msg = input()
        clientSocket.sendto(str.encode(msg), (HOST, PORT))
    clientSocket.close()


if __name__ == "__main__":
    main()