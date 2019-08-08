# http://doc.qt.io/qt-5/qudpsocket.html#QUdpSocket
# https://github.com/baoboa/pyqt5/blob/master/examples/network/broadcastreceiver.py

from PyQt5.QtCore import QObject
from PyQt5.QtNetwork import QUdpSocket
from server_controller import server_controller


class UdpServer(QObject):

	def __init__ (self, parent = None, port = 22122):
		super(UdpServer, self).__init__(parent)
		self.udpSocket = QUdpSocket(self)
		self.udpSocket.bind(port)
		self.udpSocket.readyRead.connect(self.processPendingDatagrams)


	def processPendingDatagrams(self):
		while self.udpSocket.hasPendingDatagrams():
			datagram, host, port = self.udpSocket.readDatagram(self.udpSocket.pendingDatagramSize())
			server_controller(datagram.decode("utf-8"))


