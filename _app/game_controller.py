from Data import GameState, GameRoom
from Data import In, Out1, Out2
from Game import Game
from preview import preview
from room_1 import room_1
from room_2 import room_2
from room_3 import room_3
from time import sleep

from init_controller import jerome_in 
from init_controller import jerome_out_1
from init_controller import jerome_out_2
from init_controller import back_sound 
from init_controller import voice_sound

from PyQt5.QtCore import QTimer


def game_controller():

	print(GameState(Game.state))
	if Game.state == GameState.GAME.value:
		game()
	elif Game.state == GameState.WIN.value:
		win()
	elif Game.state == GameState.LOSE.value:
		lose()
	elif Game.state == GameState.ASSEMBLE.value:
		assemble()
	elif Game.state == GameState.EMERGENCY.value:
		emergency()
	elif Game.state == GameState.SERVICE.value:
		pass


def game():
	print(GameRoom(Game.room))
	if Game.room == GameRoom.PREVIEW.value:
		preview()
	elif Game.room == GameRoom.ROOM_1.value:
		room_1()
	elif Game.room == GameRoom.ROOM_2.value:
		room_2()
	elif Game.room == GameRoom.ROOM_3.value:
		room_3()


def win():
	QTimer.singleShot(8*1000, lambda: back_sound.stop())
	QTimer.singleShot(8*1000, lambda: voice_sound.play(1))
	jerome_out_1.set_pin_high(Out1.DOOR_EXIT_MAGNET.value)
	Game.loop_flag = False

	
def lose():
	jerome_out_1.set_pin_high(Out1.DOOR_EXIT_MAGNET.value)
	Game.loop_flag = False

def assemble():
	pass

def emergency():
	pass



if __name__ == '__main__':
	print('game_controller')
	print(GameRoom(Game.room))
	print(Game.room)
		