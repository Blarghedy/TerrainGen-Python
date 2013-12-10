
import random

class DiamondSquare(object):
	def __init__(self, n, mod, seed=None):
		self.seed = seed
		self.n = n
		self.mod = mod
		if self.seed == None:
			self.arr = [[0]*n for i in range(n)]
			s = 20
			self.arr[0][0] = random.uniform(0,s)
			self.arr[0][-1] = random.uniform(0,s)
			self.arr[-1][0] = random.uniform(0,s)
			self.arr[-1][-1] = random.uniform(0,s)
			self.arr[n//2][n//2] = random.uniform(0,s)
		else:
			self.arr = [list(i) for i in self.seed]
		
	def diamond_square(self):
		n = self.n
		squares = [(0,0,n-1)] # (x, y, width)
		arr = self.arr
		newsquares = []
		
		#while squares[0][2] >= 1:
		width = n-1 # note that width is both width and height
		width *= 2  # not sure if this is necessary; probably is
		
		while width >= 1:
			#newsquares = []
			#print(squares[0][2])
			#width = squares[0][2]  # note that width is both width and height
			width = width // 2
			
			#for s in squares:
			for x0 in range(0, n-1, width):
				for y0 in range(0, n-1, width):
			
					#w = s[2]
					#x0 = s[0]
					#x1 = s[0]+s[2]
					#y0 = s[1]
					#y1 = s[1]+s[2]
					#pt_x = x0 + w//2
					#pt_y = y0 + w//2
					x1 = x0+width
					y1 = y0+width
					pt_x = x0 + width//2
					pt_y = y0 + width//2
					
					arr[pt_x][pt_y] = (arr[x0][y0] + arr[x0][y1] + arr[x1][y0] + arr[x1][y1])/4 + random.uniform(-self.mod,self.mod)
					if pt_x == 0:
						arr[-1][pt_y] = arr[pt_x][pt_y]
					elif pt_x == n-1:
						arr[0][pt_y] = arr[pt_x][pt_y]
					if pt_y == 0:
						arr[pt_x][-1] = arr[pt_x][pt_y]
					elif pt_y == n-1:
						arr[pt_x][0] = arr[pt_x][pt_y]
					if pt_x == pt_y == 0: # top left corner; do lower right
						arr[-1][-1] = arr[0][0]
					elif pt_x == pt_y == n-1: # bottom right corner; do top left
						arr[0][0] = arr[-1][-1]
					#newsquares += [(x0,y0,w//2), (x0+w//2,y0,w//2), (x0,y0+w//2,w//2), (x0+w//2,y0+w//2,w//2)]
			
			print("precision", width)
			#squares = newsquares
			if width == 1: # this is weird
				print("breaking")
				break
			oddline = False
			
			for i in range(0,n,width//2): # this is silly
				oddline = not oddline
				j = 0
				while j < n:
					if oddline and j != 0:
						j += width//2
						pass
					if j >= n:
						#print("breaking:" + str(j) + ">=" + str(n))
						break
					self.setDiamond(i, j, width//2, self.mod)
					j += width
			self.mod = self.mod*.5
		#printArray(arr)
		return arr

	def setDiamond(self, i, j, dif, mod):
		"""
		
		"""
		top = j + dif
		bottom = j - dif
		left = i - dif
		right = i + dif
		n = len(self.arr)
		
		if left < 0:
			left = n - 1 + left
		if right > n-1:
			right = 0 + 1 + (right-n)
		if bottom < 0:
			bottom = n - 1 + bottom
		if top > n-1:
			top = 0 + 1 + (top-n)
		val = (self.arr[i][top] + self.arr[i][bottom] + self.arr[left][j] + self.arr[right][j])/4 + random.uniform(-mod,mod)
			
		self.setPixel(i, j, val)

	def setPixel(self, i, j, val):
		"""
		Sets a pixel i,j to the value val.  Also takes care of overlap.
		"""
		n = len(self.arr)
		if self.arr[i][j] != 0:
			return False
		if (i == j == 0) or (i == j == n-1) or (i == 0 and j == n-1) or (i == n-1 and j == 0):
			self.arr[0][0] = val
			self.arr[0][-1] = val
			self.arr[-1][0] = val
			self.arr[-1][-1] = val
			#self.__writePixel(0,0,val)
			#self.__writePixel(0,-1,val)
			#self.__writePixel(-1,0,val)
			#self.__writePixel(-1,-1,val)
		elif i == 0:
			self.arr[-1][j] = val
			#self.__writePixel(-1,j,val)
		elif i == n-1:
			self.arr[0][j] = val
			#self.__writePixel(0,j,val)
		elif j == 0:
			self.arr[i][-1] = val
			#self.__writePixel(i,-1,val)
		elif j == n-1:
			self.arr[i][0] = val
			#self.__writePixel(i,0,val)
		self.arr[i][j] = val
		#self.__writePixel(i,j,val)
		return True

	def __writePixel(self,i,j,val):
		"""
		Writes value val to pixel i,j.  
		Used for debug purposes; will probably be deprecated in favor of explicit array access.
		"""
		self.arr[i][j] = val
		
	def printArray(arr):
		return
		#for i in arr:
			#print(", ".join(["%4.3f"%(j) for j in i])) # just print 3 digits after the decimal in each element

	def smoothArray(self,n=1):
		arr = self.arr
		lend = len(arr[0])
		for h in range(n):
			ret = [[0]*lend for d in arr]
			
			for i in range(1,len(arr)-1):
				for j in range(1,len(arr)-1):
					ret[i][j] = (arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j-1] + arr[i][j] + arr[i][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1])/9
			arr = ret
		return arr

	
		