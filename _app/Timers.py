from PyQt5.QtCore import QTimer


def action_by_timer(jerome, pin, timer):
	jerome.set_pin_high(pin)
	QTimer.singleShot(timer, lambda: jerome.set_pin_low(pin))

def action_delay(jerome, pin, value, timer):
	QTimer.singleShot(timer, lambda: jerome.set_pin(pin, value))



if __name__ == '__main__':

	import sys
	from PyQt5 import QtGui
	from init_controller import jerome_in 


	app = QtGui.QGuiApplication(sys.argv)
	action_by_timer(jerome_in, 1, 2000)
	app.exec_()
