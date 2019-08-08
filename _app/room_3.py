from Data import Define, rabbit_list, rabbit_queue, status_msg
from Data import GameState, GameRoom 
from Data import In, Out1, Out2
from Game import Game
from init_controller import jerome_in 
from init_controller import jerome_out_1
from init_controller import jerome_out_2
from init_controller import pc_strelka
from init_controller import back_sound 
from init_controller import voice_sound
from Timers import action_by_timer, action_delay
from PyQt5.QtCore import QTimer


def room_3():

	print(Game.step)

	# if Game.step != 4:
	# 	if jerome_in.get_pin(In.DOOR_EGG_GERCON.value) == Define.ACTIVATE.value:
	# 		action_by_timer(jerome_out_1, Out1.CUT_EGG_LOCK.value, 1000)

	if Game.step == 1:
		back_sound.play(2)
		QTimer.singleShot(10*1000, lambda: voice_sound.play(0))
		Game.step += 1

	if Game.step == 2:
		if Game.pc_strelka_flag == True or Game.operator_command == 301:
			if jerome_out_2.get_pin_uniq(Out2.GRID_DOWN.value) == 1:
				jerome_out_2.set_pin_low(Out2.GRID_DOWN.value)
			action_by_timer(jerome_out_2, Out2.GRID_UP.value, Define.MOVE_TIMER.value)
			jerome_out_1.set_pin_high(Out1.DOWER_CHEST_POWER.value)
			Game.step += 1

	elif Game.step == 3:
		if jerome_in.get_pin(In.DOWER_CHEST_TAMPER.value) == Define.ACTIVATE.value or Game.operator_command == 302:
			# jerome_out_1.set_pin_low(Out1.DOWER_CHEST_POWER.value)
			jerome_out_1.set_pin_high(rabbit_list[rabbit_queue[Game.rabbit_index]][1])
			jerome_out_1.set_pin_high(Out1.GUN_POWER.value)
			Game.step += 1

	elif Game.step == 4:
		status_msg[Game.state][Game.room][Game.step] = status_msg[Game.state][Game.room][Game.step][:40] + ' убито: {}/{}'.format(Game.rabbit_index, len(rabbit_queue))
		if jerome_in.get_pin(rabbit_list[rabbit_queue[Game.rabbit_index]][0]) == Define.ACTIVATE.value or Game.operator_command == 303 or Game.operator_command == 304:
			jerome_out_1.set_pin_low(rabbit_list[rabbit_queue[Game.rabbit_index]][1])
			Game.rabbit_index += 1
			Game.operator_command = 0
			if Game.rabbit_index < len(rabbit_queue):
				jerome_out_1.set_pin_high(rabbit_list[rabbit_queue[Game.rabbit_index]][1])
			else:	
				jerome_out_1.set_pin_low(Out1.GUN_POWER.value)
				jerome_out_1.set_pin_high(Out1.HIDE_DUCK_MAGNET.value)
				Game.step += 1 

	elif Game.step == 5:
		if Game.operator_command == 305:
			if jerome_in.get_pin(In.DOOR_EGG_GERCON.value) == Define.ACTIVATE.value:
				jerome_out_1.set_pin_low(Out1.CUT_EGG_LOCK.value)
				action_by_timer(jerome_out_2, Out2.SMOKE_EGG.value, Define.SMOKE_EGG_TIMER.value)

				if jerome_out_1.get_pin_uniq(Out1.CUT_EGG_UP.value) == 1:
					jerome_out_1.set_pin_low(Out1.CUT_EGG_UP.value)
				action_by_timer(jerome_out_1, Out1.CUT_EGG_DOWN.value, Define.MOVE_TIMER.value)

				action_delay(jerome_out_1, Out1.CUT_EGG_LOCK.value, Define.OPEN.value, Define.OPEN_DELAY_EGG_LOCK_TIMER.value)
				action_delay(jerome_out_1, Out1.CUT_EGG_LOCK.value, Define.CLOSE.value, Define.OPEN_DELAY_EGG_LOCK_TIMER.value + Define.EGG_LOCK_TIMER.value)

				Game.state = GameState.WIN.value
				Game.room = GameRoom.PREVIEW.value
				Game.step = 1


