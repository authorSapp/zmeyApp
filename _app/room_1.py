from Data import Define
from Data import GameState, GameRoom 
from Data import In, Out1, Out2
from Game import Game
from init_controller import jerome_in 
from init_controller import jerome_out_1
from init_controller import jerome_out_2
from init_controller import pc_window 
from init_controller import pc_apple
from init_controller import back_sound 
from init_controller import voice_sound 


# from PyQt5.QtCore import QTimer
from Timers import action_by_timer, action_delay


def room_1():

	print(Game.step)

	if Game.step == 1:
		back_sound.play(0)
		Game.step += 1
	
	elif Game.step == 2:
		if jerome_in.get_pin(In.CLOUD_GERCON.value) == Define.ACTIVATE.value or Game.operator_command == 101:
			jerome_out_1.set_pin_high(Out1.HIDE_ROOF_MAGNET.value)
			Game.step += 1 

	elif Game.step == 3:
		if jerome_in.get_pin(In.MUSHROOM_ON_OVEN.value) == Define.ACTIVATE.value or Game.operator_command == 102:
			jerome_out_1.set_pin_high(Out1.HIDE_LOWER_WALL_MAGNET.value)
			Game.step += 1 

	elif Game.step == 4:
		if jerome_in.get_pin(In.BOOTS_WINTER_BUTTON.value) == Define.ACTIVATE.value or Game.operator_command == 103:
			pc_window.send_command('winter')
			action_by_timer(jerome_out_1, Out1.FRIDGE_LIGHT_AND_MAGNET.value, Define.FRIDGE_LIGHT_AND_MAGNET_TIMER.value)
			Game.step += 1 

	elif Game.step == 5:
		if jerome_in.get_pin(In.BOOTS_AUTUMN_SPRING_BUTTON.value) == Define.ACTIVATE.value  or Game.operator_command == 104:
			pc_window.send_command('spring')
			Game.step += 1 

	elif Game.step == 6:
		if jerome_in.get_pin(In.WOOL_DEVICE_POUCHES_GERCON.value) == Define.ACTIVATE.value  or Game.operator_command == 105:
			Game.step += 1 

	elif Game.step == 7:
		if jerome_in.get_pin(In.WOOL_DEVICE_POUCHES_GERCON.value) == Define.NONE.value or Game.operator_command == 106:
			Game.counter += 1
		if Game.counter == Define.WOOL_COUNT.value:
			Game.counter = 0
			jerome_out_1.set_pin_high(Out1.HIDE_OVEN_MAGNET.value)
			action_by_timer(jerome_out_2, Out2.OVEN_FAN_LIGHT_POWER.value, Define.OVEN_FAN_LIGHT_POWER_TIMER.value)
			Game.step += 1 

	elif Game.step == 8:
		if jerome_in.get_pin(In.BOOTS_SUMMER_BUTTON.value) == Define.ACTIVATE.value  or Game.operator_command == 107:
			pc_window.send_command('summer')
			jerome_out_2.set_pin_high(Out2.WINDOW_MAGNET.value)
			Game.step += 1 

	elif Game.step == 9:
		if jerome_in.get_pin(In.APPLE_TABLE_GERCON.value) == Define.ACTIVATE.value or Game.operator_command == 108:
			Game.counter += 1
			if Game.counter > Define.APPLE_COUNT.value:
				pc_apple.send_command('apple')
				Game.counter = 0
				Game.step += 1 

	elif Game.step == 10:
		if jerome_in.get_pin(In.SKULS_GERCON.value) == Define.ACTIVATE.value or Game.operator_command == 109:
			jerome_out_1.set_pin_high(Out1.HIDE_UPPER_WALL_MAGNET.value)
			Game.step += 1 

	elif Game.step == 11:
		if jerome_in.get_pin(In.MORTAR_SCRYPT_GERCON.value) == Define.ACTIVATE.value or Game.operator_command == 110:
			action_by_timer(jerome_out_2, Out2.MORTAR_FAN_LIGHT_220V.value, Define.MORTAR_FAN_LIGHT_220V_TIMER.value)
			jerome_out_2.set_pin_high(Out2.OVEN_TACHOMETER_POWER.value)
			Game.step += 1 

	elif Game.step == 12:
		if Game.operator_command == 111:
			jerome_out_2.set_pin_low(Out2.OVEN_TACHOMETER_POWER.value)
			action_by_timer(jerome_out_2, Out2.SMOKE_OVEN.value, Define.SMOKE_OVEN_TIMER.value)
			action_by_timer(jerome_out_2, Out2.GEARWHEELS_POWER.value, Define.GEARWHEELS_POWER_TIMER.value)
			jerome_out_1.set_pin_high(Out1.DOOR_OVEN_MAGNET.value)
			Game.room = GameRoom.ROOM_2.value
			Game.step = 1 


