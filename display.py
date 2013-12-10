
def foobar():
	return 

#def draw_diamond_graphics(d):
	#from graphics import *
	#n = len(d)
	#win = GraphWin(n,n,n,autoflush=False)
	#win.flush()
	#p = None
	#ma = max([max(i) for i in d])
	#mi = min([min(i) for i in d])
	#print(ma,mi)
	#ma -= mi
	#mi = 0
	#print(ma)
		
	#for i in range(len(d)):
		#for j in range(len(d[i])):
			#p = Point(i,j)
			#v = d[i][j]
			#if v < 0:
				#p.setFill("black")
			#elif v < .1:
				#p.setFill("blue")
			#elif v < .2:
				#p.setFill("green")
			#elif v < .3:
				#p.setFill("yellow")
			#elif v < .4:
				#p.setFill("white")
			#else:
				#p.setFill("grey")
			#t = int(v/ma*255)

			#p.draw(win)
		#if (i%5):
			#win.flush()
	#win.flush()
	#return win
	
def draw_terrain_PIL(t):
	print("drawing terrain")
	nodes = t.nodes
	d = [[True]*t.length for i in range(t.length)]
	for n in nodes:
		d[n.pos[0]][n.pos[1]] = n.height
	img = draw_diamond_PIL(d)
	
	print("adding rivers to img")
	
	for n in nodes:
		if n.is_river:
			img.putpixel((n.pos[0], n.pos[1]), (200,0,0))
	
	print("returning img")
	return img
	

def draw_diamond_PIL(d):
	from PIL import Image
	"""
	Accepts d, a 2**n+1 x 2**n+1 float array and displays it using PIL.
	This is intended as a temporary measure.
	"""
	
	n = len(d)
	img = Image.new("RGB", (n,n))
	p = None
	
	ma = None
	mi = None
	av = 0
	
	for line in d:
		for i in line:
			if i != None:
				av += i
				if ma == None:
					ma = i
				elif ma < i:
					ma = i
				if mi == None:
					mi = i
				elif mi > i:
					mi = i
	
	av = av / (n*n)
	ma -= mi
	mi = 0
	
	#ma = max([max([j for j in i if j != True]) for i in d if not all(i)])
	#mi = min([min([j for j in i if j != True]) for i in d])
	#av = sum([sum([j for j in i if j != True])/n for i in d])/n
	#ma -= mi
	#mi = 0
	print("\n(min-max)",(mi,ma))
	print("average",av,"median", median([median(i) for i in d]))
	# vals = [[] for k in range(8)]
	sorted_array = []
	mean = 0
	for i in d:
		k = []
		for j in i:
			if j > 0:
				k.append(j)
		sorted_array += sorted(k)
	sorted_array.sort()
	
	lim = [0]
	lim.append(sorted_array[int(len(sorted_array)/4)])
	lim.append(sorted_array[int(.75*len(sorted_array))])
	lim.append(sorted_array[-1])
	
	lend = len(d)
	lendi = len(d[0])
	for i in range(lend):
		for j in range(lendi):
			v = d[i][j]
			r = (0,0,0)
			if v < lim[0]:
				r = (0,0,200)
			elif v < lim[1]:
				diff = lim[1]-lim[0]
				v -= lim[0]
				#g = int(250*v/diff+1)
				r = int(20+(185*v//diff))
				g = int(20+(113*v//diff))
				b = int(20+(43*v//diff))
				#r = (205,133,63) #some brown
				r = (r,g,b)
			elif v < lim[2]:
				diff = lim[2]-lim[1]
				v -= lim[1]
				g = int(150*v/diff+50)
				r = (0,g,0)
			elif v < lim[3]:
				diff = lim[3]-lim[2]
				v -= lim[2]
				g = 100+int(150*v/diff+1)
				r = (g,g,g)
			
			#print("putting",r,"at",(i,j))
			img.putpixel((i,j),r)
				
	#img.putpixel((0,0),(0,0,0))
	#val_len = [len(a) for a in vals]
	#print(val_len)
	#print([float("%3.1f"%(d*100/sum(val_len))) for d in val_len])
	#img.show()
	return img
		
def median(arr):
	"""
	Calculate and return the median of a given array
	"""
	arr = sorted(arr)
	x = len(arr)
	if x%2 == 0:
		return (arr[x//2]+arr[x//2-1])/2
	else:
		return arr[x//2]