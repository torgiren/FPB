from object import Object
from OpenGL.GL import *
class Block(Object):
	def __init__(self,posx=0,posy=0,posz=0):
		Object.__init__(self,posx,posy,posz)
		x=0
		y=0
		z=0
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
	def RetPos(self):
		return (self.x,self.y,self.z)
	def RetPoints(self):
		return self.points
