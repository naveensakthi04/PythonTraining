import socket
from time import sleep

c = socket.socket()

try:
    c.connect(('localhost', 9999))
    while True:
        print(c.recv(1024).decode())
        c.send(bytes("From client 4", "utf-8"))
        sleep(True)

except Exception as e:
    print("Connection dropped!", e)
