
import socket

print("what")

def main():
    HOST = "127.0.0.1"
    PORT = 9001

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP

    s.bind((HOST, PORT))

    # https://stackoverflow.com/questions/36325912/socket-error-errno-102-operation-not-supported-on-socket
    # s.listen()
    # connection, address = s.accept()

    #How to detect client disconnect?
    
    while True:
        msg, addr = s.recvfrom(1024)
        print(msg)
        print(addr)

if __name__ == "__main__":
    main()