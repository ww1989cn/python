import socket, P2PType,myutils


local_address = ('127.0.0.1', 10087)
remote_address = ('127.0.0.1', 10086)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(local_address)

buf = [0xFF, 0xFF,P2PType.LOGIN]

# name = 'wang'

# msg = myutils.convert_chr(buf)+name

# s.sendto(msg, remote_address)


# buf[2] = P2PType.GETALL

# s.sendto(myutils.convert_chr(buf), ('127.0.0.1', 10086))

buf = [0xFF, 0xFF,P2PType.P2PTRANS]

name = 'wei'

msg = myutils.convert_chr(buf)+name

s.sendto(msg, remote_address)

while True:
	data, addr = s.recvfrom(1024)
	
	l = list(data)
	for i  in range(3):
		l[i] = ord(l[i])

	if l[0] == 0xff and l[1]==0xff:
		t = l[2]

		if t==P2PType.GETALLACK:
			count = ord(data[-1])
			print count
		elif t==P2PType.P2PTRASH:
			print 'trash msg'
	else:
		print 'wrong package'

