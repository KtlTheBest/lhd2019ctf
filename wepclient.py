import socket
import time

HOST = "192.168.0.9"
PORT = 9002

while True:
    s = socket.socket()
    s.connect((HOST, PORT))

    print(s.recv(1024))
    s.close()
    time.sleep(5)
