import pygame
from graph import *
from block import *
from floor import *
from map import *
from pygame.locals import *
class GameEngine:
	def __init__(self):
		pygame.init()
		self.__quit=False
		self.__graph=GraphEngine()
		pygame.mouse.set_visible(False)
		self.loadMap("demo.map")
#	def __del__(self):
#		pygame.mouse.set_visible(True)
	def loadMap(self,path):
		loader=MapLoader(path)
		text=self.__graph.loadTexture("bunker2.jpg")
		floor=self.__graph.loadTexture("bunker1.jpg")
#		ceiling=self.__graph.loadTexture("bunker1.jpg")
		objs=loader.RetObjs()
		for o in objs:
			if o[2] == "wall":
				self.__graph.add_obj(Block(int(o[0]),0,int(o[1]),texture=text))
		(sizeX,sizeY)=loader.RetSize()
		print sizeX,sizeY
		for i in range(1,sizeX):
			for j in range(1, sizeY):
				self.__graph.add_obj(Floor(i,0,j,texture=floor))
				self.__graph.add_obj(Floor(i,1,j,texture=floor))
		for i in range(0,sizeX):
			self.__graph.add_obj(Block(i,0,0,texture=text))
			self.__graph.add_obj(Block(i,0,sizeY,texture=text))
		for i in range(0,sizeY):
			self.__graph.add_obj(Block(0,0,i,texture=text))
			self.__graph.add_obj(Block(sizeX,0,i,texture=text))
			

	def mainLoop(self):
		while not self.__quit:
			event = pygame.event.poll() 
			if event.type == pygame.QUIT:
				self.__quit=True
#			if event.type == pygame.MOUSEMOUTIN:
			(mousex,mousey)=pygame.mouse.get_pos()
			if mousex is not 100:
#				print float(mousex)
				delta=(float((mousex-100))/2)
				self.__graph.move(r=delta)
#				self.__graph.move(r=-self.__last_move)
#				print delta
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
