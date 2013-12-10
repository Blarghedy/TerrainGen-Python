
from diamond import DiamondSquare
from display import *
from terraingeneration import Terrain

import diamond

def main():
	
	r = 5
	v = 10
	n = 2**v+1
	seed = [[0]*n for i in range(n)]
	seed[0][0] = 2
	seed[0][-1] = 2
	seed[-1][0] = 2
	seed[-1][-1] = 2
	
	
	
	smooth = 1
	for i in range(1):
		diamond = DiamondSquare(n, r, seed)
		x = diamond.diamond_square()
		#print("in main, diamond array is")
		#DiamondSquare.printArray(x)
		#y = draw_diamond_PIL(x)
		#fname = str(i) +"_" + str(n) + "x" + str(n) + "_rand_" + str(r) + "_diamond.bmp"
		#print("saving as " + fname)
		#y.save(fname)
		print("smoothing")
		#y.show()
		z = diamond.smoothArray(3)
		print("creating terrain")
		t = Terrain(z)
		print("drawing")
		#x = draw_diamond_PIL(z)
		print(len(t.nodes), "nodes")
		x = draw_terrain_PIL(t)
		x.save(str(n) + "x" + str(n) + "_" + str(i) + "_" + "diamond_smooth_" + str(smooth) +".bmp")
		#z = x
		#for j in range(1,smooth+1):
			#z = diamond.smoothArray(10)
			##x = draw_diamond_PIL(z)
			##z.show()
			#print(str(n) + "x" + str(n) + "_" + str(i) + "_rand_" + str(r) + "_diamond_smooth_" + str(j) +".bmp")
			#x.save(str(n) + "x" + str(n) + "_" + str(i) + "_" + "diamond_smooth_" + str(j) +".bmp")
	print("done")

if __name__ == "__main__":
	main()
	#import cProfile
	#cProfile.run("main()", "terrainstats.txt")
	#import pstats
	#p = pstats.Stats("terrainstats.txt")
	#p.strip_dirs().sort_stats("time").print_stats(20)
	##p.sort_stats("ncalls")
	##p.print_stats(20)
	