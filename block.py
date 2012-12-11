from object import Object
from OpenGL.GL import *
class Block(Object):
	def __init__(self,posx=0,posy=0,posz=0,texture=None):
		Object.__init__(self,posx,posy,posz,texture)
		self.points=[]
		self.type=GL_TRIANGLES
		self.points.append((0.0,0.0,0.0,0.0,0.0))
		self.points.append((1.0,0.0,1.0,0.0,0.0))
		self.points.append((1.0,1.0,1.0,1.0,0.0))

		self.points.append((0.0,0.0,0.0,0.0,0.0))
		self.points.append((1.0,1.0,1.0,1.0,0.0))
		self.points.append((0.0,1.0,0.0,1.0,0.0))

		self.points.append((0.0,0.0,0.0,0.0,0.0))
		self.points.append((1.0,1.0,0.0,1.0,1.0))
		self.points.append((1.0,0.0,0.0,0.0,1.0))

		self.points.append((0.0,0.0,0.0,0.0,0.0))
		self.points.append((0.0,1.0,0.0,1.0,0.0))
		self.points.append((1.0,1.0,0.0,1.0,1.0))

		self.points.append((0.0,0.0,1.0,0.0,0.0))
		self.points.append((1.0,1.0,1.0,1.0,1.0))
		self.points.append((1.0,0.0,1.0,0.0,1.0))

		self.points.append((0.0,0.0,1.0,0.0,0.0))
		self.points.append((0.0,1.0,1.0,1.0,0.0))
		self.points.append((1.0,1.0,1.0,1.0,1.0))

		self.points.append((0.0,0.0,0.0,0.0,1.0))
		self.points.append((1.0,0.0,1.0,0.0,1.0))
		self.points.append((1.0,1.0,1.0,1.0,1.0))

		self.points.append((0.0,0.0,0.0,0.0,1.0))
		self.points.append((1.0,1.0,1.0,1.0,1.0))
		self.points.append((0.0,1.0,0.0,1.0,1.0))


		#self.points.append((x+0.0,y+0.0,z+0.0))
		#self.points.append((x+0.0,y+0.0,z+0.0))
		#self.points.append((x+0.0,y+0.0,z+0.0))

