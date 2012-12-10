#!/usr/bin/env python
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def render():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_TRIANGLES)
	glVertex2i(100,200)
	glVertex2i(200,200)
	glVertex2i(150,300)
	glEnd()
	glFlush()
glutInit()
glutInitWindowSize(800,600)
glutCreateWindow("First")
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutDisplayFunc(render)
glClearColor(1.0,1.0,1.0,0.0)
glColor3f(0.0,0.0,0.0)
glPointSize(2.0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0.0,800.0,0.0,600.0)
glutMainLoop()
