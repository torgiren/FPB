class Object:
	def __init__(self,x=0,y=0,z=0):
		self.__x=x
		self.__y=y
		self.__z=z
		self.texture=None
	def RetPos(self):
		return (self.__x,self.__y,self.__z)
	def SetTexture(self,texture):
		self.texture=texture
