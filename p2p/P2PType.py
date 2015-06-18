

LOGIN = 0x10
LOGOUT = 0x11
P2PTRANS = 0x12
GETALL = 0x13
GETALLACK = 0x14
USERINFO = 0x16
CALLYOU = 0x15
P2PTRANSACK = 0x17
P2PTRASH = 0x17

class Message(object):

	def setType(self, type):
		self.type = type

	def type(self):
		return self.type

	def function():
		pass