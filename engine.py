import pygame
from graph import *
from block import *
from pygame.locals import *
class GameEngine:
	def __init__(self):
		self.__quit=False
		self.__graph=GraphEngine()
		self.__graph.add_obj(Block(0,0,-5))
		self.__graph.add_obj(Block(5,0,-5))
		self.__graph.add_obj(Block(-5,0,-5))
	def mainLoop(self):
		while not self.__quit:
			pygame.event.get()
			keys=pygame.key.get_pressed()
			if keys[K_w]:
				self.__graph.move(forward=-0.05)
			if keys[K_s]:
				self.__graph.move(forward=+0.05)
			if keys[K_a]:
				self.__graph.move(side=+0.05)
			if keys[K_d]:
				self.__graph.move(side=-0.05)
			if keys[K_q]:
				self.__graph.move(r=-1.0)
			if keys[K_e]:
				self.__graph.move(r=+1.0)
			self.__graph.render()
			pygame.time.delay(20)
			
		
