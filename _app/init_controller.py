import Data
from Jerome import Jerome
from Computer import Computer
from Game import Game 
from Sound import Sound
from PyQt5.QtMultimedia import QMediaPlaylist


# jerome_in = Jerome()
jerome_in = Jerome(Data.Jerome.IN.value)
jerome_out_1 = Jerome(Data.Jerome.OUT_1.value)
jerome_out_2 = Jerome(Data.Jerome.OUT_2.value)

pc_strelka = Computer(Data.Computer.STRELKA.value)
pc_window = Computer(Data.Computer.WINDOW.value)
pc_apple = Computer(Data.Computer.APPLE.value)
# pc_center_head = Computer(Data.Computer.CENTER_HEAD.value)
# pc_left_head = Computer(Data.Computer.LEFT_HEAD.value)
# pc_right_head = Computer(Data.Computer.RIGHT_HEAD.value)

back_sound = Sound(Data.Sound.BACK_SOUND.value, QMediaPlaylist.CurrentItemInLoop)
voice_sound = Sound(Data.Sound.VOICE_SOUND.value, QMediaPlaylist.CurrentItemOnce)


if __name__ == '__main__':
	print('init_controller')
	print(Game.room)