

PC_OPERATOR = '192.168.0.165'

text = ''
word_1_flag = False
word_2_flag = False

from pynput import keyboard
import socket
import sys
import traceback


class UdpClient:

	def __init__ (self, ip = '127.0.0.1', port = 22122):

		self.ip = ip
		self.port = port
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #for UDP
		# self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #for TCP
		self.sock.settimeout(1.0)
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
		try:
			self.sock.sendto(cmd.encode('utf-8'),(self.ip, self.port)) # for UDP
			# self.sock.send(cmd.encode('utf-8')) # for TCP
			print(self.ip + ' send command: ' + cmd)
		except:
			print('Send error to ' + self.ip)
			traceback.print_exc(file=sys.stdout)


# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

def on_release(key):

	global text
	global word_1_flag
	global word_2_flag

	try:
		if key.char in 'qwertyuiop[]asdfghjkl;\'\\zxcvbnm,./1234567890-=':
			text += key.char
	except AttributeError:
		if key == keyboard.Key.space:
			text += ' '
		elif key == keyboard.Key.backspace:
			text = text[:-1]
		elif key == keyboard.Key.enter:
			if word_1_flag == False:
				if text[-5:] == 'cnegf':
					udpClient.send_command('open_left_head')
					word_1_flag = True
					print('word_1')

			if word_1_flag == True and word_2_flag == False:
				if text[-5:] == 'b;bwf':
					udpClient.send_command('open_right_head')
					word_2_flag = True
					print('word_2')
					return False
			text = ''
		else:
			return True
		
	print(text)





if __name__ == '__main__':

	# udpClient = UdpClient(PC_OPERATOR)
	udpClient = UdpClient()
	with keyboard.Listener(
			# on_press=on_press,
			on_release=on_release) as listener:
		listener.join()


