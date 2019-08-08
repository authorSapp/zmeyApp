

PC_OPERATOR = '192.168.0.165'


import sys
import traceback

from PyQt5.QtCore import Qt 
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QLabel, QLineEdit, QApplication)
# from PyQt5.QtGui import QIcon

class MainHead(QWidget):
	
	def __init__(self):
		super().__init__()
		self.initUI()
		
	def initUI(self):

		self.setWindowTitle('Main Head')
		self.setGeometry(100, 100, 800, 600)
		# self.setWindowIcon(QIcon('./logo.png'))
		self.setStyleSheet("QWidget { background-color: rgb(49, 56, 66); }")

		self.lbl = QLabel(self)
		self.lbl.move((self.frameGeometry().width()-270)/2, (self.frameGeometry().height()-0)/2)
		self.lbl.setText('Введите кодовое слово:')
		self.lbl.setStyleSheet("QLabel { font: 24px; color: rgb(150, 150, 150);}")

		self.qle = QLineEdit(self)
		self.qle.setAttribute(Qt.WA_MacShowFocusRect, False)
		self.qle.resize(300,60)
		self.qle.move((self.frameGeometry().width()-300)/2, (self.frameGeometry().height()-80)/2)
		self.qle.setAlignment(Qt.AlignHCenter)
		self.qle.setMaxLength(10)
		self.qle.setStyleSheet("QLineEdit { background-color: white; font: bold 32px; color: rgb(66, 66, 66); border-color: rgb(49, 56, 166); border-radius: 12px; }")
		# self.qle.setPlaceholderText('Введите код')
		# self.qle.setFocusPolicy(Qt.ClickFocus)
		# self.qle.setFrame(False)

		self.qle.textChanged[str].connect(self.onChanged)
 		
		# self.showFullScreen()
		self.show()

	   
	def resizeEvent(self, event):
		self.qle.move((self.frameGeometry().width()-300)/2, (self.frameGeometry().height()-80)/2)
		self.lbl.move((self.frameGeometry().width()-270)/2, (self.frameGeometry().height()-180)/2)

	def onChanged(self, text):
		self.qle.setText(text.upper())
		main_controller(text.upper())





import socket

class UdpClient:

	def __init__ (self, ip = '127.0.0.1', port = 22122):

		self.ip = ip
		self.port = port
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #for UDP
		# self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #for TCP
		self.sock.settimeout(1.0)
		# self.sock.connect((ip, port))
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
			self.sock.sendto(cmd.encode('utf-8'),(self.ip, self.port))
			# self.sock.send(cmd.encode('utf-8'))
			print(self.ip + ' send command: ' + cmd)
		except:
			print('Send error to ' + self.ip)
			traceback.print_exc(file=sys.stdout)





from PyQt5.QtCore import QObject
from PyQt5.QtNetwork import QUdpSocket

class UdpServer(QObject):

	def __init__ (self, parent = None, port = 22122):
		super(UdpServer, self).__init__(parent)
		self.udpSocket = QUdpSocket(self)
		self.udpSocket.bind(port)
		self.udpSocket.readyRead.connect(self.processPendingDatagrams)


	def processPendingDatagrams(self):
		while self.udpSocket.hasPendingDatagrams():
			datagram, host, port = self.udpSocket.readDatagram(self.udpSocket.pendingDatagramSize())
			recieve_data_controller(datagram.decode("utf-8"))




 
def main_controller(text):
	if (text == 'СТУПА'):
		udpClient.send_command('open_left_head')
		QTimer.singleShot(1000, lambda: window.qle.setText(''))
	elif (text == 'ИЖИЦА'):
		udpClient.send_command('open_right_head')
		QTimer.singleShot(1000, lambda: window.qle.setText(''))


def recieve_data_controller(recieve_data):
	print('recieve data: ' + recieve_data)
	if recieve_data == 'reset':
		window.qle.setText('')



if __name__ == '__main__':
	app = QApplication(sys.argv)
	udpServer = UdpServer()
	udpClient = UdpClient(PC_OPERATOR)
	window = MainHead()
	sys.exit(app.exec_())


