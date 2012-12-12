from object import Object
from OpenGL.GL import *
class Block(Object):
	def __init__(self,posx=0,posy=0,posz=0,texture=None):
		Object.__init__(self,posx,posy,posz,texture)
		self.points=[]
		self.type=GL_TRIANGLES
		self.VBO=True
		self.VBO_Buf=None

		self.points.extend((0.0,0.0,0.0,0.0,0.0))
		self.points.extend((0.0,0.0,0.0,0.0,0.0))
	
		self.points.extend((1.0,0.0,1.0,0.0,0.0))
		self.points.extend((1.0,1.0,1.0,1.0,0.0))

		self.points.extend((0.0,0.0,0.0,0.0,0.0))
		self.points.extend((1.0,1.0,1.0,1.0,0.0))
		self.points.extend((0.0,1.0,0.0,1.0,0.0))

		self.points.extend((0.0,0.0,0.0,0.0,0.0))
		self.points.extend((1.0,1.0,0.0,1.0,1.0))
		self.points.extend((1.0,0.0,0.0,0.0,1.0))

		self.points.extend((0.0,0.0,0.0,0.0,0.0))
		self.points.extend((0.0,1.0,0.0,1.0,0.0))
		self.points.extend((1.0,1.0,0.0,1.0,1.0))

		self.points.extend((0.0,0.0,1.0,0.0,0.0))
		self.points.extend((1.0,1.0,1.0,1.0,1.0))
		self.points.extend((1.0,0.0,1.0,0.0,1.0))

		self.points.extend((0.0,0.0,1.0,0.0,0.0))
		self.points.extend((0.0,1.0,1.0,1.0,0.0))
		self.points.extend((1.0,1.0,1.0,1.0,1.0))

		self.points.extend((0.0,0.0,0.0,0.0,1.0))
		self.points.extend((1.0,0.0,1.0,0.0,1.0))
		self.points.extend((1.0,1.0,1.0,1.0,1.0))

		self.points.extend((0.0,0.0,0.0,0.0,1.0))
		self.points.extend((1.0,1.0,1.0,1.0,1.0))
		self.points.extend((0.0,1.0,0.0,1.0,1.0))
		self.points.extend((1.0,0.0,1.0,0.0,0.0))
		self.points.extend((1.0,1.0,1.0,1.0,0.0))

		self.points.extend((0.0,0.0,0.0,0.0,0.0))
		self.points.extend((1.0,1.0,1.0,1.0,0.0))
		self.points.extend((0.0,1.0,0.0,1.0,0.0))

		self.points.extend((0.0,0.0,0.0,0.0,0.0))
		self.points.extend((1.0,1.0,0.0,1.0,1.0))
		self.points.extend((1.0,0.0,0.0,0.0,1.0))

		self.points.extend((0.0,0.0,0.0,0.0,0.0))
		self.points.extend((0.0,1.0,0.0,1.0,0.0))
		self.points.extend((1.0,1.0,0.0,1.0,1.0))

		self.points.extend((0.0,0.0,1.0,0.0,0.0))
		self.points.extend((1.0,1.0,1.0,1.0,1.0))
		self.points.extend((1.0,0.0,1.0,0.0,1.0))

		self.points.extend((0.0,0.0,1.0,0.0,0.0))
		self.points.extend((0.0,1.0,1.0,1.0,0.0))
		self.points.extend((1.0,1.0,1.0,1.0,1.0))

		self.points.extend((0.0,0.0,0.0,0.0,1.0))
		self.points.extend((1.0,0.0,1.0,0.0,1.0))
		self.points.extend((1.0,1.0,1.0,1.0,1.0))

		self.points.extend((0.0,0.0,0.0,0.0,1.0))
		self.points.extend((1.0,1.0,1.0,1.0,1.0))
		self.points.extend((0.0,1.0,0.0,1.0,1.0))
		self.size=len(self.points)


		#self.points.append((x+0.0,y+0.0,z+0.0))
		#self.points.append((x+0.0,y+0.0,z+0.0))
		#self.points.append((x+0.0,y+0.0,z+0.0))

