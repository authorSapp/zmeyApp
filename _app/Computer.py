import socket
import sys
import traceback

class Computer:

	def __init__ (self, ip = '127.0.0.1', port = 22122):

		self.ip = ip
		self.port = port
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.settimeout(2.0)
		self.sock.connect((ip, port))
		try:
			self.sock.connect((ip, port))
			print('Connect to Comp ' + self.ip)
		except:
			print('Error connect Comp ' + self.ip)
			traceback.print_exc(file=sys.stdout)
			

	def __del__ (self):
		self.sock.close()
		print('Disconnect from Comp ' + self.ip)

	def send_command(self, cmd):
		self.sock.sendto(cmd.encode('utf-8'),(self.ip, self.port))
		# self.sock.send(cmd.encode('utf-8'))
		print(self.ip + ' send command: ' + cmd)



if __name__ == '__main__':
	print('class Computer')
	local_host = Computer()
	local_host.send_command('Hello')