import socket
import sys
import traceback

class Jerome:

	def __init__ (self, ip = '192.168.0.250', port = 2424):

		self.ip = ip
		self.port = port
		
		self.sock = socket.socket()
		self.sock.settimeout(1.0)
		try:
			self.sock.connect((ip, port))
			print('Connect to Jerome ' + self.ip)
		except:
			print('Error connect Jerome ' + self.ip)
			traceback.print_exc(file=sys.stdout)



	def __del__ (self):
		self.sock.close()
		print('Disconnect from Jerome ' + self.ip)


	def command(self, data, param_1 = '', param_2 = ''):
		comma_1 = '' if param_1 == '' else ','
		comma_2 = '' if param_2 == '' else ','
		cmd = "$KE,{0}{1}{2}{3}{4}\r\n".format(data, comma_1, param_1, comma_2, param_2).encode('utf-8')
		print(cmd)
		return cmd

	def recieve_result(self):
		result = self.sock.recv(256).decode("utf-8")
		print(result)
		if result == '#SLINF\r\n':
			result = self.recieve_result()
		return result

	#for OUT pin
	def set_pin_high(self, lineNumber):
		self.sock.send(self.command('WR', lineNumber, 1))
		return self.recieve_result()

	#for OUT pin
	def set_pin_low(self, lineNumber):
		self.sock.send(self.command('WR', lineNumber, 0))
		return self.recieve_result()

	def set_pin(self, lineNumber, value):
		self.sock.send(self.command('WR', lineNumber, value))
		return self.recieve_result()

	#for OUT pins
	#example mask - 10100 10101 11010 11111 xx
	# 22 chars whithout space
	# x - don't change pin, 1 - set high, 0 - set low
	def set_pin_by_mask(self, mask):
		self.sock.send(self.command('WRA', mask))
		return self.recieve_result()

	#for OUT pins
	def set_all_pins_high(self):
		self.sock.send(self.command('WR,ALL,ON'))
		return self.recieve_result()

	#for OUT pins
	def set_all_pins_low(self):
		self.sock.send(self.command('WR,ALL,OFF'))
		return self.recieve_result()

	#for IN pin
	#answer: #RD,02,1
	def get_pin(self, lineNumber):
		self.sock.send(self.command('RD', lineNumber))
		return int(self.recieve_result()[-3: -2])

	#for ALL pins, get info only IN pins
	#answer: #RD,xxx10xxx0xxx1xxxxxxxxx
	def get_all_pins(self):
		self.sock.send(self.command('RD,ALL'))
		return self.recieve_result()[-24: -2]

	#get info for ANY pin
	#answer: #RID,05,1
	def get_pin_uniq(self, lineNumber):
		self.sock.send(self.command('RID', lineNumber))
		return int(self.recieve_result()[-3: -1])


	#get info for ANY pins
	#answer: #RID,ALL,0001011100111110011111
	def get_all_pins_uniq(self):
		self.sock.send(self.command('RID,ALL'))
		return self.recieve_result()[-24: -2]

	#answer: #RID,IN,xxx10xxx0xxx1xxxxx1111
	def get_all_pins_which_in(self):
		self.sock.send(self.command('RID,IN'))
		return self.recieve_result()[-24: -2]

	#answer: #RID,OUT,000xx111x011x11001xxxx
	def get_all_pins_which_out(self):
		self.sock.send(self.command('RID,OUT'))
		return self.recieve_result()[-24: -2]

	# powerValue = 0% - 100%
	def set_pwm(self, powerValue):
		self.sock.send(self.command('PWM,SET', powerValue))
		return self.recieve_result()

	#answer: #PWM,60
	def get_pwm(self, powerValue):
		self.sock.send(self.command('PWM,GET'))
		return int(self.recieve_result()[5: None])

	# frequency = 651_042/(value+1)
	def set_pwm_frequency(self, value):
		self.sock.send(self.command('PFR,SET', value))
		return self.recieve_result()

	#answer: #PFR,156
	def get_pwm_frequency(self):
		self.sock.send(self.command('PFR,GET'))
		return int(self.recieve_result()[6: None])

	#for ANY pin
	def set_pin_in(self, lineNumber):
		self.sock.send(self.command('IO,SET', lineNumber, 1))
		return self.recieve_result()

	#for ANY pin
	def set_pin_out(self, lineNumber):
		self.sock.send(self.command('IO,SET', lineNumber, 0))
		return self.recieve_result()

	#for ALL pins
	def set_all_pins_in(self):
		self.sock.send(self.command('IO,SET,ALL,IN'))
		return self.recieve_result()

	#for ALL pins
	def set_all_pins_out(self):
		self.sock.send(self.command('IO,SET,ALL,OUT'))
		return self.recieve_result()

	#answer: #IO,ALL,0001000011000000000000
	def get_direction_for_all_pins(self):
		self.sock.send(self.command('IO,GET,ALL'))
		return self.recieve_result()[-24: -2]

	#store size 265 byte (address = 0 - 255)
	#data size not more 32 byte! 
	def set_eeprom_data(self, address, data):
		self.sock.send(self.command('UDT,SET', address, "{}{}".format(len(data), data)))
		return self.recieve_result()

	#length = 1 - 32
	def get_eeprom_data(self, address, length):
		self.sock.send(self.command('UDT,GET', address, length))
		return self.recieve_result()

	def event_on(self):
		self.sock.send(self.command('EVT,ON'))
		return self.recieve_result()

	def event_off(self):
		self.sock.send(self.command('EVT,OFF'))
		return self.recieve_result()

	def device_info(self):
		self.sock.send(self.command('INF'))
		return self.recieve_result()

	def device_reset(self):
		self.sock.send(self.command('RST'))
		return self.recieve_result()



if __name__ == '__main__':
	print('class Jerome')
	j_test = Jerome()
	print(j_test.device_info())



