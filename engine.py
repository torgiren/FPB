import pygame
from graph import *
from block import *
from pygame.locals import *
class GameEngine:
	def __init__(self):
		pygame.init()
		self.__quit=False
		self.__graph=GraphEngine()
		self.__graph.add_obj(Block(0,0,-5))
		self.__graph.add_obj(Block(5,0,-5))
		self.__graph.add_obj(Block(-5,0,-5))
		pygame.mouse.set_visible(False)
	def __del__(self):
		pygame.mouse.set_visible(True)
	def mainLoop(self):
		while not self.__quit:
			event = pygame.event.poll() 
			if event.type == pygame.QUIT:
				self.__quit=True
#			if event.type == pygame.MOUSEMOUTIN:
			(mousex,mousey)=pygame.mouse.get_pos()
			if mousex is not 100:
				print float(mousex)
				delta=(float((mousex-100))/2)
				self.__graph.move(r=delta)
#				self.__graph.move(r=-self.__last_move)
				print delta
				pygame.mouse.set_pos((100,100))

			keys=pygame.key.get_pressed()
			speed=1
			if keys[K_ESCAPE]:
				self.__quit=True
			if keys[K_LSHIFT]:
				speed=2
			if keys[K_w]:
				self.__graph.move(forward=-0.05*speed)
			if keys[K_s]:
				self.__graph.move(forward=+0.05*speed)
			if keys[K_a]:
				self.__graph.move(side=+0.03*speed)
			if keys[K_d]:
				self.__graph.move(side=-0.03*speed)
			self.__graph.render()
			pygame.time.delay(20)
			
		