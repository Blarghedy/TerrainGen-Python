
from random import choice

class Terrain(object):
	def __init__(self, d=None):
		self.nodes = []
		self.num_rivers = 50
		self.length = 0
		# assume d is either None or a 2D array of height values
		if d != None:
			self.length = len(d)
			d = [[i for i in j] for j in d]
			self.convert_from_2D_array(d)

	def convert_to_2D_array(self,d=None):
		pass

	def convert_from_2D_array(self,d=None):
		# create a node for each position and store it in a 2D array
		print("converting array")
		for i in range(len(d)):
			for j in range(len(d[i])):
				node = Node((i,j), d[i][j])
				d[i][j] = node
				self.nodes.append(node)

		# add each node to its right and bottom neighbors
		# this takes care of the top and left neighbors as well
		print("find neighbors")
		for i in range(len(d)-1):
			for j in range(len(d[i])-1):
				d[i][j].add_node(d[i][j+1])
				d[i][j].add_node(d[i+1][j])

		# now loop each edge
		for i in range(len(d[-1])):
			d[-1][i].add_node(d[0][i])
		for i in range(len(d)):
			d[i][-1].add_node(d[i][0])

		# at this point, all nodes are aware of their neighbors
		# so now we need to discover certain properties of each node 
		# to start, find shore nodes
		print("finding shore nodes")
		for n in self.nodes:
			if not n.is_ocean:
				for line in n.lines:
					# this is a bit ugly; only one check should be necessary
					if line.left.is_ocean or line.right.is_ocean:
						n.is_shore = True
						break
		# find shore edges 
		# a list of all lines would greatly ease this project

		print("finding shore lines")
		for n in self.nodes:
			if n.is_shore:
				for line in n.lines:
					if line.left.is_shore and line.right.is_shore:
						line.is_shore = True

		# now that we know all shores, find every ocean
		# skipping this for now
		#oceans = []
		#i = 0
		#lennodes = len(self.nodes)
		#while i < lennodes:
			#n = self.nodes[i]
			#if n.is_ocean:
				#for o in n.others():
					#n.add_node(o)
				#del self.nodes[i]
			#else:
				#i += 1
			#lennodes = len(self.nodes)

		# generate rivers
		# we should have self.num_rivers rivers, so generate some random points
		# make sure each point is on land
		#print("generate rivers")
		#river_nodes = []
		#while len(river_nodes) < self.num_rivers:
			#n = choice(self.nodes)
			#if not (n.is_ocean or n in river_nodes):
				#n.is_river = True
				#river_nodes.append(n)
				
		#for i in range(len(river_nodes)):
			#print(i, river_nodes[i].pos, river_nodes[i].height)
			
		# each river will start at a river node, but now we have to actually make the rivers
		# a simple algorithm is just to follow the path of least resistance
		# or, more specifically, the edge with the lowest 
		#for r in river_nodes:
			#n = r
			#lake = []
			#while not n.is_ocean:
				#tmp_nodes = n.others()
				#tmp_nodes.sort() # this should use Node.__lt__ automatically
				####print(n.others())
				#tmp_nodes[0].is_river = True 
				##l = n.get_line(tmp_nodes[0])
				##l.is_river = True
				#if tmp_nodes[0] > n:  # we've fallen into a hole 
					#break 
					#height = tmp_nodes[0].height
					
					##find all non-wet neighbors
					##tmp_nodes = [tmp_nodes[0]] + [node for node in tmp_nodes[0].others() if not node.is_wet] 
					
					##while True: #find lakes
						##break
				#else:
					#n = tmp_nodes[0]
					#lake = []
					
	def create_lake(self, r_node):
		pass

	

class Node(object):
	def __init__(self, pos, height):
		#print("node: ", pos, height)
		self.pos = pos
		self.is_shore = False
		self.is_lake = False
		self.is_river = False
		self.lines = []
		self.height = height
		if height <= 0:
			self.is_ocean = True
		else:
			self.is_ocean = False
	is_wet = property(lambda self: self.is_ocean or self.is_river or self.is_lake)

	def add_node(self, n):
		line = Line(self, n)
		if line not in self.lines:
			self.lines.append(line)
			n.lines.append(line)
			return n
		else:
			return None
		
	#def rem_node(self, n):
		#for line in self.lines:
			#if n in line.nodes
		
	def get_line(self, n):
		others = self.others()
		for line in others:
			if line.left == n or line.right == n:
				return line
		return None

	def other(self, line):
		if self == line.left:
			return line.right
		elif self == line.right:
			return line.left
		else:
			return None

	def others(self):
		ret = [self.other(line) for line in self.lines]
		return ret

	def __lt__(self, n):
		return self.height < n.height

	def __gt__(self, n):
		return self.height > n.height

	def __le__(self, n):
		return self.height <= n.height

	def __ge__(self, n):
		return self.height >= n.height



class Line(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right
		self.is_ocean = False
		self.is_shore = False

	def __eq__(self, other):
		return self.left == other.left and self.right == other.right
