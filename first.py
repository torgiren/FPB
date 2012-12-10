#!/usr/bin/env python
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

def render():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_TRIANGLES)
	glVertex3f(-1.0,0.0,-10)
	glVertex3f(1.0,0.0,-10)
	glVertex3f(0.0,1.0,-10)
	glEnd()
	pygame.display.flip()
pygame.init()
pygame.display.set_mode((800,600),HWSURFACE|OPENGL|DOUBLEBUF)
glViewport(0,0,800,600)


#glutInit()
#glutInitWindowSize(800,600)
#glutCreateWindow("First")
#glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
#glutDisplayFunc(render)
glClearColor(1.0,1.0,1.0,0.0)
glColor3f(0.0,0.0,0.0)
glPointSize(2.0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective( 60.0, float( 800 ) / float( 600 ), 0.1, 1000.0 )
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
while True:
	render()
	pygame.time.delay(100)
#gluOrtho2D(0.0,800.0,0.0,600.0)
#glutMainLoop()
