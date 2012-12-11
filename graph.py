from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import math
class GraphEngine:
	def __init__(self):
		pygame.display.set_mode((800,600),HWSURFACE|OPENGL|DOUBLEBUF)
#		glEnable(GL_LIGHTING)
#		glEnable(GL_LIGHT0)
#		glLightfv(GL_LIGHT1,GL_POSITION,[0,0,-9])
#		glEnable(GL_LIGHT1)
#		glEnable(GL_COLOR_MATERIAL)
		glShadeModel(GL_SMOOTH)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_TEXTURE_2D)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)



		glViewport(0,0,800,600)
		glClearColor(0.3,0.3,0.3,0.0)
		glColor3f(1.0,1.0,1.0)
		glPointSize(2.0)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective( 60.0, float( 800 ) / float( 600 ), 0.1, 1000.0 )
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def del_textures(self,objs):
		for o in objs:
			glDeleteTextures(o.RetTexture())
	def render(self,objs,pos):
		glLoadIdentity()	
		glRotatef(pos[3],0,1,0)
		glTranslatef(pos[0],pos[1],pos[2])
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		for o in objs:
			p=o.RetPos()
#			print p
			if abs(p[0]+pos[0])<10 and abs(p[2]+pos[2])<10:
				self.draw(o)
		pygame.display.flip()
	def draw(self,obj):
		glPushMatrix()
#		glLoadIdentity()
		pos=obj.RetPos()
		glTranslate(*pos)
		points=obj.RetPoints()
		glBindTexture(GL_TEXTURE_2D, obj.RetTexture())
		glBegin(obj.RetType())
		for p in points:
			glTexCoord2f(p[0],p[1])
			glVertex3f(p[2],p[3],p[4])
		glEnd()
		glPopMatrix()
	def loadTexture(self,path):
		surf=pygame.image.load(path)
		data=pygame.image.tostring(surf,"RGBA",1)
		width=surf.get_width()
		height=surf.get_height()
		texture=glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D,texture)
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
		return texture
