import socket

PORT = 50000
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('172.20.10.10', PORT))
    s.send(b'hello!')
    print(repr(s.recv(BUFFER_SIZE)))
