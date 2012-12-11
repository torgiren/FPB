class MapLoader:
	def __init__(self,path):
		f=open(path,"r")
		line=f.readline()
		line=line.split()
		self.__sizeX=line[0]
		self.__sizeY=line[1]
		line=f.readline()
		line=line.split()
		self.__startX=line[0]
		self.__startY=line[1]
		self.__objs=[]
		while True:
			line=f.readline()
			if not line:
				break
			line=line.split()
			if len(line)==3:
				self.__objs.append(line)
			else:
				print "Map error"
				print line
				exit(1)
	def RetObjs(self):
		return self.__objs
	def RetSize(self):
		return (int(self.__sizeX),int(self.__sizeY))
	def RetStart(self):
		return (int(self.__startX), int(self.__startY))
