from object import Object
from OpenGL.GL import *
class Block(Object):
	def __init__(self,posx=0,posy=0,posz=0,texture=None):
		Object.__init__(self,posx,posy,posz)
		if texture:
			self.SetTexture(texture)
		x=0
		y=0
		z=0
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

	def RetType(self):
		return self.type
	def RetPoints(self):
		return self.points
