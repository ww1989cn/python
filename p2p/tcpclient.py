import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 8082))

s.connect(('127.0.0.1', 8120))



data = s.recv(1024)

print data

s.close()