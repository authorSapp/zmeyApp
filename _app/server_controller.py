from Game import Game

def server_controller(recieve_data):
	if recieve_data == 'strelka':
		Game.pc_strelka_flag = True
	elif recieve_data == 'open_left_head':
		Game.pc_main_head_flag = 1
	elif recieve_data == 'open_right_head':
		Game.pc_main_head_flag = 2