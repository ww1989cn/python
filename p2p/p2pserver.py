#!/usr/bin/env python
# -*- coding:utf-8 -*-

'a p2p server on udp'

__Author__ = 'Wang'

import socket, P2PType, myutils


class User(object):

	def setName(self, name):
		self.name = name

	def name(self):
		return self.name

	def setIP(self, ip):
		self.ip = ip

	def IP(self):
		return self.ip

	def setPort(self, port):
		self.port = port

	def port(self):
		return self.port

users = []


server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_sock.bind(('127.0.0.1', 10086))

print 'Server start...'

while True:
	data, addr = server_sock.recvfrom(1024)
	print 'received from %s:%s' %addr

	l = list(data)
	for i  in range(3):
		l[i] = ord(l[i])

	if l[0] == 0xff and l[1]==0xff:
		t = l[2]
		

		if t==P2PType.LOGIN:
			name = data[3:]

			user = User()
			user.setName(name)
			user.setIP(addr[0])
			user.setPort(addr[1])
			users.append(user)
			print 'new user login!'
		elif t==P2PType.GETALL:
			buf = [0xFF, 0xFF,P2PType.GETALLACK]
			msg = myutils.convert_chr(buf)+chr(len(users))
			server_sock.sendto(msg, addr)
	else:
		print 'wrong package'


