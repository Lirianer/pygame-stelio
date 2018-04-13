class Rectangle():

	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def setWidth(self, width):
		self.width = width

	def setHeight(self, height):
		self.height = height

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def top(self):
		return self.y
	
	def bottom(self):
		return self.y + self.height
	
	def left(self):
		return self.x

	def right(self):
		return self.x + self.width
