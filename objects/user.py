class User():
	def __init__(self, eID, username, secret, addr, conn):
		self.eID = eID
		self.username = username
		self.secret = secret
		self.addr = addr
		self.conn = conn
		self.channel = None
		self.timesRequestedHistory = 0