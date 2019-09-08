#!/usr/bin/env python3

import socket

def main():
    HOST = "127.0.0.1"
    PORT = 9001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with s:
        s.connect((HOST, PORT))
        while True:
            i = input()
            s.send(str.encode(i))
            


if __name__ == "__main__":
    main()