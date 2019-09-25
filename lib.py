

def read_udp(conn):
    data = ""

    (ch, addr) = conn.recvfrom(1)
    while ch != "\0".encode() and ch != "".encode():
        data += ch.decode()
        (ch, addr) = conn.recvfrom(1)
    return data, addr


def send_udp(data, conn, HOST, PORT):
    for ch in data:
        conn.sendto(ch.encode(), (HOST, PORT))
    conn.sendto("\0".encode(), (HOST, PORT))