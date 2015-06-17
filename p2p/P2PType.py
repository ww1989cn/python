

LOGIN = 0x10
LOGIN = 0x11
P2PTRANS = 0x12
GETALL = 0x13
GETALLACK = 0x14

class Message(object):

	def setType(self, type):
		self.type = type

	def type(self):
		return self.type

	def function():
		pass