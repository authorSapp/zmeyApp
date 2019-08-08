from Data import Define
from Data import GameState, GameRoom 
from Data import In, Out1, Out2
from Game import Game
from init_controller import jerome_in 
from init_controller import jerome_out_1
from init_controller import jerome_out_2
# from init_controller import pc_center_head 
# from init_controller import pc_left_head 
# from init_controller import pc_right_head 
from init_controller import back_sound 
from init_controller import voice_sound 

from Timers import action_by_timer


def room_2():

	print(Game.step)

	if Game.step == 1:
		back_sound.play(1)
		Game.step += 1

	elif Game.step == 2:
		if Game.pc_main_head_flag == 1 or Game.operator_command == 201:
			if jerome_out_2.get_pin_uniq(Out2.LEFT_HEAD_DOWN.value) == 1:
				jerome_out_2.set_pin_low(Out2.LEFT_HEAD_DOWN.value)
			action_by_timer(jerome_out_1, Out1.LEFT_HEAD_UP.value, Define.MOVE_TIMER.value)
			Game.pc_main_head_flag == 0
			Game.step += 1

	elif Game.step == 3:
		if Game.pc_main_head_flag == 2 or Game.operator_command == 202:
			if jerome_out_2.get_pin_uniq(Out2.RIGHT_HEAD_DOWN.value) == 1:
				jerome_out_2.set_pin_low(Out2.RIGHT_HEAD_DOWN.value)
			action_by_timer(jerome_out_1, Out1.RIGHT_HEAD_UP.value, Define.MOVE_TIMER.value)
			Game.pc_main_head_flag == 0
			Game.step += 1

	elif Game.step == 4:
		if Game.operator_command == 203:
			jerome_out_1.set_pin_high(Out1.DOOR_2_3_MAGNET.value)
			Game.room = GameRoom.ROOM_3.value
			Game.step = 1 

