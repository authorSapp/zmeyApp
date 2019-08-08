from PyQt5 import QtGui
from PyQt5.QtCore import QUrl, QFileInfo
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
import sys


class Sound:

	def __init__ (self, tracks_url_list, play_back_mode):
		
		self.list = list

		self.playlist = QMediaPlaylist()
		for track_url in tracks_url_list:
			self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(QFileInfo(track_url).absoluteFilePath())))
		self.playlist.setPlaybackMode(play_back_mode)
	
		self.player = QMediaPlayer()
		self.player.setPlaylist(self.playlist)

	def __del__ (self):
		self.player.stop()


	def play(self, item):
		self.playlist.setCurrentIndex(item)
		self.player.play()

	def stop(self):
		self.player.stop()



if __name__ == '__main__':

	app = QtGui.QGuiApplication(sys.argv)

	tracks_url = ["./sound/1.mp3", "./sound/2.mp3", "./sound/3.mp3"]
	sound = Sound(tracks_url)
	sound.play(2)
	input()
	sound.play(0)

	app.exec_()


