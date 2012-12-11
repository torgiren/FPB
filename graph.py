from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import math
class GraphEngine:
	def __init__(self):
		pygame.display.set_mode((800,600),HWSURFACE|OPENGL|DOUBLEBUF)
		glEnable(GL_LIGHTING)
#		glEnable(GL_LIGHT0)
		glLightfv(GL_LIGHT1,GL_POSITION,[0,0,-9])
		glEnable(GL_LIGHT1)
		glEnable(GL_COLOR_MATERIAL)
		glShadeModel(GL_SMOOTH)
		glEnable(GL_DEPTH_TEST)
		glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.7, 0.7, 0.7, 0])
		glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.8, 0.8, 0.7, 0])
		glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.8, 0.8, 0.8, 0])
		glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 30)
		glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE); 
		glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, 0)

		glLightModeli( GL_LIGHT_MODEL_COLOR_CONTROL, GL_SEPARATE_SPECULAR_COLOR )
		glLightfv(GL_LIGHT0, GL_POSITION, [-5, -3, -10, 0])
		glLightfv(GL_LIGHT0, GL_AMBIENT, [0, 0, 0, 0])
		glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 0])
		glLightfv(GL_LIGHT0, GL_SPECULAR, [0.8, 0.8, 0.8, 0])

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

		self.__objs=[]
		self.__x=0
		self.__y=-0.5
		self.__z=0
		self.__r=0
	def render(self):
		glLoadIdentity()
		glRotatef(self.__r,0,1,0)
		glTranslatef(self.__x,self.__y,self.__z)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		for o in self.__objs:
			self.draw(o)
		pygame.display.flip()
	def draw(self,obj):
		glPushMatrix()
#		glLoadIdentity()
		pos=obj.RetPos()
		glTranslate(*pos)
		points=obj.RetPoints()
		glBegin(obj.RetType())
		for p in points:
			glVertex3f(*p)
		glEnd()
		glPopMatrix()
	def add_obj(self,obj):
		self.__objs.append(obj)
	def move(self,forward=0,y=0,side=0,r=0):
		self.__x+=forward*math.sin(math.radians(self.__r))
		self.__x+=side*math.cos(math.radians(self.__r))
		self.__y+=y
		self.__z-=forward*math.cos(math.radians(self.__r))
		self.__z+=side*math.sin(math.radians(self.__r))
		self.__r+=r
