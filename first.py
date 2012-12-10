#!/usr/bin/env python
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

class obj:
	def __init__(self,x=0,y=0,z=0):
		self.__x=x
		self.__y=y
		self.__z=z
class Block(obj):
	def __init__(self,x=0,y=0,z=0):
		obj.__init__(self,x,y)
		self.points=[]
		self.type=GL_TRIANGLES
		self.points.append((x+0.0,y+0.0,z+0.0))
		self.points.append((x+1.0,y+0.0,z+0.0))
		self.points.append((x+1.0,y+1.0,z+0.0))

		self.points.append((x+0.0,y+0.0,z+0.0))
		self.points.append((x+1.0,y+1.0,z+0.0))
		self.points.append((x+0.0,y+1.0,z+0.0))

		self.points.append((x+0.0,y+0.0,z+0.0))
		self.points.append((x+0.0,y+1.0,z-1.0))
		self.points.append((x+0.0,y+0.0,z-1.0))

		self.points.append((x+0.0,y+0.0,z-0.0))
		self.points.append((x+0.0,y+1.0,z-0.0))
		self.points.append((x+0.0,y+1.0,z-1.0))

		self.points.append((x+1.0,y+0.0,z+0.0))
		self.points.append((x+1.0,y+1.0,z-1.0))
		self.points.append((x+1.0,y+0.0,z-1.0))

		self.points.append((x+1.0,y+0.0,z-0.0))
		self.points.append((x+1.0,y+1.0,z-0.0))
		self.points.append((x+1.0,y+1.0,z-1.0))

		self.points.append((x+0.0,y+0.0,z-1.0))
		self.points.append((x+1.0,y+0.0,z-1.0))
		self.points.append((x+1.0,y+1.0,z-1.0))

		self.points.append((x+0.0,y+0.0,z-1.0))
		self.points.append((x+1.0,y+1.0,z-1.0))
		self.points.append((x+0.0,y+1.0,z-1.0))


		#self.points.append((x+0.0,y+0.0,z+0.0))
		#self.points.append((x+0.0,y+0.0,z+0.0))
		#self.points.append((x+0.0,y+0.0,z+0.0))

	def RetType(self):
		return self.type
	def RetPoints(self):
		return self.points
class GraphEngine:
	def __init__(self):
		pass	
	def draw(self,obj):
		glBegin(obj.RetType())
		points=obj.RetPoints()
		for p in points:
			glVertex3f(*p)
		glEnd()
			

pygame.init()
pygame.display.set_mode((800,600),HWSURFACE|OPENGL|DOUBLEBUF)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glViewport(0,0,800,600)
glClearColor(1.0,1.0,1.0,0.0)
glColor3f(0.0,0.0,0.0)
glPointSize(2.0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective( 60.0, float( 800 ) / float( 600 ), 0.1, 1000.0 )
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
graph=GraphEngine()
block=Block(z=-5,y=-2,x=-2)
while True:
	pygame.time.delay(100)
	glClear(GL_COLOR_BUFFER_BIT)
	graph.draw(block)
	pygame.display.flip()
