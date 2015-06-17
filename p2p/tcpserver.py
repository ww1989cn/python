#!/usr/bin/env python
# -*- coding:utf-8 -*-

'tcp server'

__Author__='Wang'

import socket, threading
from db import MyDatabase


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(('127.0.0.1', 8120))

s.listen(5)

print 'Waiting for connection...'


def tcplink(sock, addr):
	print 'accept new connection from %s:%s' %addr

	#db.add('11', '%s:%s' %addr)

	#db = MyDatabase()

	#values = db.query()

	#print values

	sock.send("%s:%s" %addr)

	sock.close()


while True:
	sock, addr = s.accept()
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()





