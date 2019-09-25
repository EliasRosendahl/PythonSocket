import threading

from UDPserver import UDPServer



def main():
    servers = [
        #UDPServer('127.0.0.1', 9000),
        UDPServer('127.0.0.1', 9001)
        ]

    for s in servers:
        t = threading.Thread(target=s.run)
        t.start()
        




if __name__ == "__main__":
    main()