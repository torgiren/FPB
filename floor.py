from object import Object
from OpenGL.GL import *
class Floor(Object):
	def __init__(self,posx=0,posy=0,posz=0,texture=None):
		Object.__init__(self,posx,posy,posz,texture)
		self.point=[]
		self.VBO=True
		self.VBO_Buf=None
		self.size=0
		self.type=GL_TRIANGLES
		self.points.append((0.0,0.0,0.0,0.0,0.0))
		self.points.append((1.0,1.0,1.0,0.0,1.0))
		self.points.append((0.0,1.0,0.0,0.0,1.0))
		
		self.points.append((0.0,0.0,0.0,0.0,0.0))
		self.points.append((1.0,0.0,1.0,0.0,0.0))
		self.points.append((1.0,1.0,1.0,0.0,1.0))
		self.size=len(self.points)
