class Object:
	def __init__(self,x=0,y=0,z=0,texture=None):
		self.type=None
		self.texture=None
		self.points=[]
		if texture:
			self.SetTexture(texture)
		self.__x=x
		self.__y=y
		self.__z=z
	def RetPos(self):
		return (self.__x,self.__y,self.__z)
	def SetTexture(self,texture):
		self.texture=texture
	def RetTexture(self):
		return self.texture
	def RetType(self):
		return self.type
	def RetPoints(self):
		return self.points
