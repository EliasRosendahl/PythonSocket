
import socket

print("what")

def main():
    HOST = "127.0.0.1"
    PORT = 9001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()

    #How to detect client disconnect?
    with connection:
        print("Connection from: ", address)
        while True:
            data = connection.recv(1024)
            print(data)

if __name__ == "__main__":
    main()