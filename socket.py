import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 1234))
sock.listen(True)

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    data = bytes.decode(data)
    s1 = ""
    for i in data:
        if ord(i) + 1 > ord("я"):
            s1 += chr(ord(i) + 1 - 32)
        else:
            s1 += chr(ord(i) + 1)
    s2 = str.encode(s1)
    conn.sendall(s2)
    time.sleep(1)
