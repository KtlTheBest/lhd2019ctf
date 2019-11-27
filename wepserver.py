import socket

s = socket.socket()
HOST = "192.168.0.9"
PORT = 9002

s.bind((HOST, PORT))

s.listen(5)

while True:
    c, addr = s.accept()
    print("{} connected".format(addr))
    c.send("Just-doing-some-sending")
