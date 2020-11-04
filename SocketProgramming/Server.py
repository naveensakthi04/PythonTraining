import socket

s = socket.socket()
print("Socket created")

s.bind(('localhost', 9999))
s.listen(5)
print("Waiting for connections...")

while True:
    c, addr = s.accept()
    print("Connected with", addr)

    c.send(bytes('Hello world!', 'utf-8'))
    print(addr, ":", c.recv(1024).decode())
