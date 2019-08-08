from enum import Enum, auto

# class Data:

# 	def __init__(self):
# 		self.GameState = self.GameState()
# 		self.GameRoom = self.GameRoom()
# 		self.In = self.In()
# 		self.Out1 = self.Out1()
# 		self.Out2 = self.Out2()
# 		self.Jerome = self.Jerome()
# 		self.Computer = self.Computer()




class Define(Enum):
	TIME_LOOP = 128

	ACTIVATE = 0
	NONE = 1
	OPEN = 1
	CLOSE = 0
	APPLE_COUNT = 1
	WOOL_COUNT = 5

	SMOKE_EGG_TIMER = 5*1000 #msec
	SMOKE_OVEN_TIMER = 5*1000 #msec
	FRIDGE_LIGHT_AND_MAGNET_TIMER = 60*1000 #msec
	OVEN_FAN_LIGHT_POWER_TIMER = 10*1000 #msec
	MORTAR_FAN_LIGHT_220V_TIMER = 30*1000 #msec
	GEARWHEELS_POWER_TIMER = 180*1000 #msec
	MOVE_TIMER = 10*1000 #msec
	EGG_LOCK_TIMER = 200 #msec
	OPEN_DELAY_EGG_LOCK_TIMER = 7*1000 #msec


class GameState(Enum):
	GAME = 0
	WIN = 1
	LOSE = 2
	ASSEMBLE = 3
	EMERGENCY = 4
	SERVICE = 5


class GameRoom(Enum):
	PREVIEW = 0
	ROOM_1 = 1
	ROOM_2 = 2
	ROOM_3 = 3


class In(Enum):
	# APPLE_TABLE_GERCON = 1 #old #pin don't work
	BOOTS_SUMMER_BUTTON = 2
	BOOTS_AUTUMN_SPRING_BUTTON = 3
	BOOTS_WINTER_BUTTON = 4
	DOWER_CHEST_TAMPER = 5
	RABBIT_1 = 6
	RABBIT_2 = 7
	MUSHROOM_ON_OVEN = 8 # old pin RABBIT_3 = 8
	RABBIT_4 = 9
	DOOR_EGG_GERCON = 10
	SKULS_GERCON = 11
	CLOUD_GERCON = 12
	WINDOW_GERCON = 13
	RESERVE_1 = 14
	RESERVE_2 = 15
	RESERVE_3 = 16
	WOOL_DEVICE_POUCHES_GERCON = 17
	MORTAR_SCRYPT_GERCON = 18
	WOOD_IN_OVEN = 19
	# MUSHROOM_ON_OVEN = 20 #old #pin don't work
	APPLE_TABLE_GERCON = 21
	# MUSHROOM_ON_OVEN = 22 #pin don't work


class Out1(Enum):
	FRIDGE_LIGHT_AND_MAGNET = 1
	RESERVE_1 = 2
	HIDE_UPPER_WALL_MAGNET = 3
	HIDE_LOWER_WALL_MAGNET = 4
	HIDE_ROOF_MAGNET = 5
	HIDE_OVEN_MAGNET = 6
	DOOR_OVEN_MAGNET = 7
	LEFT_HEAD_UP = 8
	RIGHT_HEAD_UP = 9
	DOOR_2_3_MAGNET = 10
	GUN_POWER = 11
	DOOR_EXIT_MAGNET = 12
	HIDE_DUCK_MAGNET = 13
	DOWER_CHEST_POWER = 14
	RABBIT_1_POWER = 15
	RABBIT_2_POWER = 16
	RABBIT_3_POWER = 17
	RABBIT_4_POWER = 18
	CUT_EGG_DOWN = 19
	CUT_EGG_UP = 20
	CUT_EGG_LOCK = 21 # 1-open
	RESERVE_2 = 22


class Out2(Enum):
	MORTAR_FAN_LIGHT_220V = 1
	SMOKE_EGG = 2
	# WOOD_IN_OVEN_XXX = 3
	# WOOL_DEVICE = 4
	GEARWHEELS_POWER = 5
	# UF = 6
	RESERVE_1 = 7
	RESERVE_2 = 8
	GRID_UP = 9
	GRID_DOWN = 10
	LEFT_HEAD_DOWN = 11
	RIGHT_HEAD_DOWN = 12
	RESERVE_3 = 13
	RESERVE_4 = 14
	OVEN_FAN_LIGHT_POWER = 15
	PUMPS_POWER = 16
	SMOKE_OVEN = 17
	OVEN_TACHOMETER_POWER = 18
	# RESERVE_5 = "don't use"
	# RESERVE_6 = "don't use"
	# RESERVE_7 = "don't use"
	WINDOW_MAGNET = 22


class Jerome(Enum):
	IN = '192.168.0.160'
	OUT_1 = '192.168.0.161'
	OUT_2 = '192.168.0.162'


class Computer(Enum):
	STRELKA = '192.168.0.150'
	WINDOW = '192.168.0.151'
	APPLE = '192.168.0.152'
	CENTER_HEAD = '192.168.0.153'
	LEFT_HEAD = '192.168.0.154'
	RIGHT_HEAD = '192.168.0.155'
	OPERATOR = '192.168.0.165'

class Sound(Enum):
	BACK_SOUND = ["./sound/1.mp3", "./sound/2.mp3", "./sound/3.mp3"]
	VOICE_SOUND = ["./sound/cash_pr.mp3", "./sound/win.mp3"]


rabbit_queue = [2, 4, 1, 4, 2]

rabbit_list = [
				[None, None],
				[In.RABBIT_1.value, Out1.RABBIT_1_POWER.value],
				[In.RABBIT_2.value, Out1.RABBIT_2_POWER.value],
				[None, None], # [In.RABBIT_3.value, Out1.RABBIT_3_POWER.value],
				[In.RABBIT_4.value, Out1.RABBIT_4_POWER.value],
			]

status_msg = [

	[
		[
			'',
			'',
		],

		[
			'',
			'',
			'Ожидаем пока тыкнут в облако...',
			'Ожидаем пока повесят грибы...',
			'Ожидаем пока наденут валенки...',
			'Ожидаем пока наденут калоши...',
			'Ожидаем пока положат мешочки в веретено...',
			'Ожидаем пока покрутят веретено...',
			'Ожидаем пока наденут лапти...',
			'Ожидаем пока яблоком покрутят по тарелке...',
			'Ожидаем пока выставят все черепа...',
			'Ожидаем пока разгадают ступу...',
			'Ожидаем пока нажмут кнопки на печи...'
		],

		[
			'',
			'',
			'Ожидаем пока введут "ступа"...',
			'Ожидаем пока введут "ижица"...',
			'Ждем пока змей долетит до замка кощея...'
		],

		[
			'',
			'',
			'Ожидаем пока решат головоломку...',
			'Ожидаем пока поставят сундук на место...',
			'Ожидаем пока перестреляют всех зайцев...',
			'Ожидаем пока положат яйцо и закроют дверцу...'
		],
	],


	[
		[
			'',
			'Игра закончена. Игроки выиграли.'
		]
	],


	[
		[
			'',
			'Игра закончена. Игроки проиграли.'
		]
	]

]

if __name__ == '__main__':

	import Data

	print('class Data')
	print(list(Data.Jerome))
	print(list(Data.Computer))
	print(Data.Jerome.IN.name)
	print(Data.Jerome.IN.value)

