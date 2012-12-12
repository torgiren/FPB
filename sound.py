import pygame
class SoundEngine:
	def __init__(self):
		pygame.mixer.init(frequency=10000)
		self.sounds={}
	def load(self,name,path):
		self.sounds[name]=pygame.mixer.Sound(path)
	def play(self,name,loop=0):
		self.sounds[name].play(loop)
	def stop(self,name):
		self.sounds[name].stop()
		
