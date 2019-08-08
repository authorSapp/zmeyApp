# import *.ui to *.py
# python3 -m PyQt5.uic.pyuic /Users/admin/Documents/gui_zmey.ui -o /Users/admin/Google\ Диск/_PyCharm_Projects/_zmeyApp/_union/gui.py -x


# from PyQt5 import sip 

import sys
import time
import traceback
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon

import gui

from Data import Define
from Data import GameState, GameRoom 
from Data import In, Out1, Out2
from Data import status_msg, rabbit_queue
from Game import Game
# from Signal import Signal
from init_controller import jerome_in 
from init_controller import jerome_out_1
from init_controller import jerome_out_2
from init_controller import pc_strelka 
from init_controller import pc_window 
from init_controller import pc_apple 
from init_controller import back_sound 

from game_controller import game_controller
from Timers import action_by_timer, action_delay

from UdpServer import UdpServer


class Zmey_app(QtWidgets.QMainWindow, gui.Ui_MainWindow):

	def __init__(self):
		super().__init__()

		# self.signal = Signal()
		# self.signal.your_signal.connect(self.action_your_signal)

		self.setupUi(self)

		self.stepButton_001.clicked.connect(self.func_stepButton)
		self.stepButton_101.clicked.connect(self.func_stepButton)
		self.stepButton_102.clicked.connect(self.func_stepButton)
		self.stepButton_103.clicked.connect(self.func_stepButton)
		self.stepButton_104.clicked.connect(self.func_stepButton)
		self.stepButton_105.clicked.connect(self.func_stepButton)
		self.stepButton_106.clicked.connect(self.func_stepButton)
		self.stepButton_107.clicked.connect(self.func_stepButton)
		self.stepButton_108.clicked.connect(self.func_stepButton)
		self.stepButton_109.clicked.connect(self.func_stepButton)
		self.stepButton_110.clicked.connect(self.func_stepButton)
		self.stepButton_111.clicked.connect(self.func_stepButton)
		self.stepButton_201.clicked.connect(self.func_stepButton)
		self.stepButton_202.clicked.connect(self.func_stepButton)
		self.stepButton_203.clicked.connect(self.func_stepButton)
		self.stepButton_301.clicked.connect(self.func_stepButton)
		self.stepButton_302.clicked.connect(self.func_stepButton)
		self.stepButton_303.clicked.connect(self.func_stepButton)
		self.stepButton_304.clicked.connect(self.func_stepButton)
		self.stepButton_305.clicked.connect(self.func_stepButton)

		self.actionButton_101.clicked.connect(self.func_actionButton)
		self.actionButton_102.clicked.connect(self.func_actionButton)
		self.actionButton_103.clicked.connect(self.func_actionButton)
		self.actionButton_104.clicked.connect(self.func_actionButton)
		self.actionButton_105.clicked.connect(self.func_actionButton)
		self.actionButton_106.clicked.connect(self.func_actionButton)
		self.actionButton_107.clicked.connect(self.func_actionButton)
		self.actionButton_108.clicked.connect(self.func_actionButton)
		self.actionButton_109.clicked.connect(self.func_actionButton)
		self.actionButton_110.clicked.connect(self.func_actionButton)
		self.actionButton_111.clicked.connect(self.func_actionButton)
		self.actionButton_201.clicked.connect(self.func_actionButton)
		self.actionButton_202.clicked.connect(self.func_actionButton)
		self.actionButton_203.clicked.connect(self.func_actionButton)
		self.actionButton_204.clicked.connect(self.func_actionButton)
		self.actionButton_205.clicked.connect(self.func_actionButton)
		self.actionButton_301.clicked.connect(self.func_actionButton)
		self.actionButton_302.clicked.connect(self.func_actionButton)
		self.actionButton_303.clicked.connect(self.func_actionButton)
		self.actionButton_304.clicked.connect(self.func_actionButton)
		self.actionButton_305.clicked.connect(self.func_actionButton)
		self.actionButton_306.clicked.connect(self.func_actionButton)
		self.actionButton_307.clicked.connect(self.func_actionButton)

		self.otherButton_001.clicked.connect(self.func_otherButton)
		self.otherButton_002.clicked.connect(self.func_otherButton)
		self.otherButton_003.clicked.connect(self.func_otherButton)
		self.otherButton_004.clicked.connect(self.func_otherButton)
		self.otherButton_005.clicked.connect(self.func_otherButton)
		self.otherButton_006.clicked.connect(self.func_otherButton)
		self.otherButton_007.clicked.connect(self.func_otherButton)

		self.upTimeButton.clicked.connect(self.func_changeTimeLimitButton)
		self.downTimeButton.clicked.connect(self.func_changeTimeLimitButton)



		self.stepButton_001.clicked.connect(self.func_logStepButton)
		self.stepButton_101.clicked.connect(self.func_logStepButton)
		self.stepButton_102.clicked.connect(self.func_logStepButton)
		self.stepButton_103.clicked.connect(self.func_logStepButton)
		self.stepButton_104.clicked.connect(self.func_logStepButton)
		self.stepButton_105.clicked.connect(self.func_logStepButton)
		self.stepButton_106.clicked.connect(self.func_logStepButton)
		self.stepButton_107.clicked.connect(self.func_logStepButton)
		self.stepButton_108.clicked.connect(self.func_logStepButton)
		self.stepButton_109.clicked.connect(self.func_logStepButton)
		self.stepButton_110.clicked.connect(self.func_logStepButton)
		self.stepButton_111.clicked.connect(self.func_logStepButton)
		self.stepButton_201.clicked.connect(self.func_logStepButton)
		self.stepButton_202.clicked.connect(self.func_logStepButton)
		self.stepButton_203.clicked.connect(self.func_logStepButton)
		self.stepButton_301.clicked.connect(self.func_logStepButton)
		self.stepButton_302.clicked.connect(self.func_logStepButton)
		self.stepButton_303.clicked.connect(self.func_logStepButton)
		self.stepButton_304.clicked.connect(self.func_logStepButton)
		self.stepButton_305.clicked.connect(self.func_logStepButton)

		self.actionButton_101.clicked.connect(self.func_logActionButton)
		self.actionButton_102.clicked.connect(self.func_logActionButton)
		self.actionButton_103.clicked.connect(self.func_logActionButton)
		self.actionButton_104.clicked.connect(self.func_logActionButton)
		self.actionButton_105.clicked.connect(self.func_logActionButton)
		self.actionButton_106.clicked.connect(self.func_logActionButton)
		self.actionButton_107.clicked.connect(self.func_logActionButton)
		self.actionButton_108.clicked.connect(self.func_logActionButton)
		self.actionButton_109.clicked.connect(self.func_logActionButton)
		self.actionButton_110.clicked.connect(self.func_logActionButton)
		self.actionButton_111.clicked.connect(self.func_logActionButton)
		self.actionButton_201.clicked.connect(self.func_logActionButton)
		self.actionButton_202.clicked.connect(self.func_logActionButton)
		self.actionButton_203.clicked.connect(self.func_logActionButton)
		self.actionButton_204.clicked.connect(self.func_logActionButton)
		self.actionButton_205.clicked.connect(self.func_logActionButton)
		self.actionButton_301.clicked.connect(self.func_logActionButton)
		self.actionButton_302.clicked.connect(self.func_logActionButton)
		self.actionButton_303.clicked.connect(self.func_logActionButton)
		self.actionButton_304.clicked.connect(self.func_logActionButton)
		self.actionButton_305.clicked.connect(self.func_logActionButton)
		self.actionButton_306.clicked.connect(self.func_logActionButton)
		self.actionButton_307.clicked.connect(self.func_logActionButton)



	def func_stepButton(self):
		
		sender = self.sender().objectName()

		if sender == 'stepButton_001':
			Game.loop_flag = True
			Game.room = GameRoom.ROOM_1.value
			Game.step = 1

		elif sender == 'stepButton_101':
			Game.operator_command = 101

		elif sender == 'stepButton_102':
			Game.operator_command = 102
	
		elif sender == 'stepButton_103':
			Game.operator_command = 103
	
		elif sender == 'stepButton_104':
			Game.operator_command = 104
	
		elif sender == 'stepButton_105':
			Game.operator_command = 105
	
		elif sender == 'stepButton_106':
			Game.operator_command = 106
	
		elif sender == 'stepButton_107':
			Game.operator_command = 107
	
		elif sender == 'stepButton_108':
			Game.operator_command = 108

		elif sender == 'stepButton_109':
			Game.operator_command = 109

		elif sender == 'stepButton_110':
			Game.operator_command = 110

		elif sender == 'stepButton_111':
			Game.operator_command = 111

		elif sender == 'stepButton_201':
			Game.operator_command = 201

		elif sender == 'stepButton_202':
			Game.operator_command = 202

		elif sender == 'stepButton_203':
			Game.operator_command = 203

		elif sender == 'stepButton_301':
			Game.operator_command = 301

		elif sender == 'stepButton_302':
			Game.operator_command = 302

		elif sender == 'stepButton_303':
			Game.operator_command = 303

		elif sender == 'stepButton_304':
			Game.rabbit_index = len(rabbit_queue) - 1
			Game.operator_command = 304

		elif sender == 'stepButton_305':
			Game.operator_command = 305



	def func_actionButton(self, pressed):
		
		sender = self.sender().objectName()
		# sender = self.sender().objectName()[-3:] #optimization
		# print("{} - {}".format(sender, pressed))
		pin_value = 1 if pressed else 0

		if sender == 'actionButton_101':
			jerome_out_1.set_pin(Out1.HIDE_ROOF_MAGNET.value, pin_value)

		elif sender == 'actionButton_102':
			jerome_out_1.set_pin(Out1.FRIDGE_LIGHT_AND_MAGNET.value, pin_value)

		elif sender == 'actionButton_103':
			jerome_out_1.set_pin(Out1.HIDE_UPPER_WALL_MAGNET.value, pin_value)

		elif sender == 'actionButton_104':
			jerome_out_1.set_pin(Out1.HIDE_LOWER_WALL_MAGNET.value, pin_value)

		elif sender == 'actionButton_105':
			jerome_out_1.set_pin(Out1.HIDE_OVEN_MAGNET.value, pin_value)

		elif sender == 'actionButton_106':
			jerome_out_2.set_pin(Out2.WINDOW_MAGNET.value, pin_value)

		elif sender == 'actionButton_107':
			pc_window.send_command('winter')

		elif sender == 'actionButton_108':
			pc_window.send_command('spring')

		elif sender == 'actionButton_109':
			pc_window.send_command('summer')

		elif sender == 'actionButton_110':
			pc_apple.send_command('apple')

		elif sender == 'actionButton_111':
			jerome_out_1.set_pin(Out1.DOOR_OVEN_MAGNET.value, pin_value)

		elif sender == 'actionButton_201':
			if jerome_out_2.get_pin_uniq(Out2.LEFT_HEAD_DOWN.value) == 1:
				jerome_out_2.set_pin_low(Out2.LEFT_HEAD_DOWN.value)
				self.actionButton_202.setChecked(False)
			jerome_out_1.set_pin(Out1.LEFT_HEAD_UP.value, pin_value)

		elif sender == 'actionButton_202':
			if jerome_out_1.get_pin_uniq(Out1.LEFT_HEAD_UP.value) == 1:
				jerome_out_1.set_pin_low(Out1.LEFT_HEAD_UP.value)
				self.actionButton_201.setChecked(False)
			jerome_out_2.set_pin(Out2.LEFT_HEAD_DOWN.value, pin_value)

		elif sender == 'actionButton_203':
			if jerome_out_2.get_pin_uniq(Out2.RIGHT_HEAD_DOWN.value) == 1:
				jerome_out_2.set_pin_low(Out2.RIGHT_HEAD_DOWN.value)
				self.actionButton_204.setChecked(False)
			jerome_out_1.set_pin(Out1.RIGHT_HEAD_UP.value, pin_value)

		elif sender == 'actionButton_204':
			if jerome_out_1.get_pin_uniq(Out1.RIGHT_HEAD_UP.value) == 1:
				jerome_out_1.set_pin_low(Out1.RIGHT_HEAD_UP.value)
				self.actionButton_203.setChecked(False)
			jerome_out_2.set_pin(Out2.RIGHT_HEAD_DOWN.value, pin_value)

		elif sender == 'actionButton_205':
			jerome_out_1.set_pin(Out1.DOOR_2_3_MAGNET.value, pin_value)

		elif sender == 'actionButton_301':
			if jerome_out_2.get_pin_uniq(Out2.GRID_DOWN.value) == 1:
				jerome_out_2.set_pin_low(Out2.GRID_DOWN.value)
				self.actionButton_302.setChecked(False)
			jerome_out_2.set_pin(Out2.GRID_UP.value, pin_value)

		elif sender == 'actionButton_302':
			if jerome_out_2.get_pin_uniq(Out2.GRID_UP.value) == 1:
				jerome_out_2.set_pin_low(Out2.GRID_UP.value)
				self.actionButton_301.setChecked(False)
			jerome_out_2.set_pin(Out2.GRID_DOWN.value, pin_value)

		elif sender == 'actionButton_303':
			jerome_out_1.set_pin(Out1.HIDE_DUCK_MAGNET.value, pin_value)

		elif sender == 'actionButton_304':
			if jerome_out_1.get_pin_uniq(Out1.CUT_EGG_DOWN.value) == 1:
				jerome_out_1.set_pin_low(Out1.CUT_EGG_DOWN.value)
				self.actionButton_305.setChecked(False)
			jerome_out_1.set_pin(Out1.CUT_EGG_UP.value, pin_value)

		elif sender == 'actionButton_305':
			if jerome_out_1.get_pin_uniq(Out1.CUT_EGG_UP.value) == 1:
				jerome_out_1.set_pin_low(Out1.CUT_EGG_UP.value)
				self.actionButton_304.setChecked(False)
			jerome_out_1.set_pin(Out1.CUT_EGG_DOWN.value, pin_value)

		elif sender == 'actionButton_306':
			action_by_timer(jerome_out_1, Out1.CUT_EGG_LOCK.value, Define.EGG_LOCK_TIMER.value)

		elif sender == 'actionButton_307':
			jerome_out_1.set_pin(Out1.DOOR_EXIT_MAGNET.value, pin_value)


	def func_otherButton(self):
		
		sender = self.sender().objectName()

		if sender == 'otherButton_001':
			Game.loop_flag = False
			Game.time = 0

			Game.state = GameState.GAME.value
			Game.room = GameRoom.PREVIEW.value
			Game.step = 1

			Game.counter = 0
			Game.operator_command = 0

			Game.pc_strelka_flag = False
			Game.pc_main_head_flag = 0
			Game.rabbit_index = 0

			jerome_out_1.set_all_pins_low()
			jerome_out_2.set_all_pins_low()
			pc_strelka.send_command('reboot_strelka')
			pc_window.send_command('reboot_window')
			pc_apple.send_command('reboot_apple')

			self.time_label.setText("00:00")
			self.logTextEdit.clear()
			back_sound.stop()

			self.actionButton_101.setChecked(False)
			self.actionButton_102.setChecked(False)
			self.actionButton_103.setChecked(False)
			self.actionButton_104.setChecked(False)
			self.actionButton_105.setChecked(False)
			self.actionButton_106.setChecked(False)
			# self.actionButton_107.setChecked(False)
			# self.actionButton_108.setChecked(False)
			# self.actionButton_109.setChecked(False)
			# self.actionButton_110.setChecked(False)
			self.actionButton_111.setChecked(False)
			self.actionButton_201.setChecked(False)
			self.actionButton_202.setChecked(False)
			self.actionButton_203.setChecked(False)
			self.actionButton_204.setChecked(False)
			self.actionButton_205.setChecked(False)
			self.actionButton_301.setChecked(False)
			self.actionButton_302.setChecked(False)
			self.actionButton_303.setChecked(False)
			self.actionButton_304.setChecked(False)
			self.actionButton_305.setChecked(False)
			self.actionButton_306.setChecked(False)
			self.actionButton_307.setChecked(False)

		elif sender == 'otherButton_002':
			pc_strelka.send_command('reboot_strelka')

		elif sender == 'otherButton_003':
			pc_window.send_command('reboot_window')

		elif sender == 'otherButton_004':
			pc_apple.send_command('reboot_apple')

		elif sender == 'otherButton_005':
			Game.room = GameRoom.ROOM_1.value
			Game.step = 1
			Game.loop_flag = True

		elif sender == 'otherButton_006':
			Game.room = GameRoom.ROOM_2.value
			Game.step = 1
			Game.loop_flag = True

		elif sender == 'otherButton_007':
			Game.room = GameRoom.ROOM_3.value
			Game.step = 1
			Game.loop_flag = True



	def func_changeTimeLimitButton(self):
		
		sender = self.sender().objectName()

		if sender == 'upTimeButton':
			if Game.time_limit < 90*60:
				Game.time_limit += 120
			else:
				Game.time_limit = 90*60
			self.time_limit_label.setText("Предельное время игры: {:0>2d} мин.".format(Game.time_limit//60))
		
		elif sender == 'downTimeButton':
			if Game.time_limit > 60*60:
				Game.time_limit -= 120
			else:
				Game.time_limit = 60*60
			self.time_limit_label.setText("Предельное время игры: {:0>2d} мин.".format(Game.time_limit//60))



	def func_logStepButton(self):
		sender = self.sender()
		if sender.objectName() == 'stepButton_001':
			self.logging(1, "Старт, игра началась...")
		else:
			self.logging(1, "пропустить {}".format(sender.text()))


	def func_logActionButton(self):
		sender = self.sender()
		if sender.isChecked():
			self.logging(1, "вкл. {}".format(sender.text()))
		else:
			self.logging(1, "выкл. {}".format(sender.text()))


	def loop(self):

		try:
			if Game.loop_flag:
				game_controller()
		except:
			print('Unexpected error')
			log = open('log.txt', 'a')
			log.write('='*80 + '\n')
			log.write(time.strftime('%Y-%m-%d, %H:%M:%S') + '\n')
			log.write('-'*80 + '\n')
			traceback.print_exc(file=log)
			traceback.print_exc(file=sys.stdout)
			log.close()

	def time_controller(self):
		if Game.loop_flag:
			Game.time += 1 
			self.time_label.setText("{:0>2d}:{:0>2d}".format(Game.time//60, Game.time%60))
			if Game.time > Game.time_limit:
				Game.state = GameState.LOSE.value

	def status_bar_info(self):
		self.statusbar.showMessage(status_msg[Game.state][Game.room][Game.step])
		# self.centralwidget.setStyleSheet("[accessibleName=\"stepButton_{}{:0>2d}\"]{}".format(Game.room, Game.step, '{font: bold 12px;}'))
		# self."stepButton_{}{:0>2d}".format(Game.room, Game.step).setStyleSheet("color: red;")
		# print("QPushButton[accessibleName=\"stepButton_{}{:0>2d}\"]{}".format(Game.room, Game.step, '{font: bold 12px;}'))

	def logging(self, user, msg):
		if user:
			self.logTextEdit.appendPlainText("Оператор: {}".format(msg))
		else:
			self.logTextEdit.appendPlainText("Игрок: {}".format(msg))



def run_app():

	app = QtWidgets.QApplication(sys.argv)
	app.setWindowIcon(QIcon('logo.png'))
	window = Zmey_app()

	time_loop = QTimer()
	time_loop.timeout.connect(window.loop)
	time_loop.start(Define.TIME_LOOP.value)

	time = QTimer()
	time.timeout.connect(window.time_controller)
	time.timeout.connect(window.status_bar_info)
	time.start(1000)

	udpServer = UdpServer()

	window.show()
	app.exec_()




if __name__ == '__main__':

	run_app()



