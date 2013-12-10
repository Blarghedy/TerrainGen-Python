TerrainGen-Python
==========
About halfway through 2012, I decided to try my hand at terrain generation to get an idea of how it works.  I wanted to start with an early algorithm, possibly add a framework to make expanding to different algorithms easier, and add additional functionality.  I did some research and found the Diamond-Square algorithm, which operates in two phases:  The diamond phase and the square phase.  

The diamond phase assumes 4 starting corners (each corner of the map).  Take an average of these values and add a small value in the range [-n, +n].  Store it in the center of the map.  This creates four diamonds (more or less; it's much more obvious in later steps).  The first diamond has its right corner at the center, the top corner at the top left, the bottom corner at the bottom left, and the left corner at the center again, wrapped around the left side.  The right diamond is the same, but with the top and bottom right corners, and wrapping around the right side of the map.  The top and bottom diamonds should be obvious.  With these four diamonds, repeat the averaging step, but store the values in the middles of the diamonds.  After this squaring step, there are a total of 9 points calculated.  Decrease the range [-n, +n] by some percentage; the steeper the percentage, the more jagged the resulting land will be.  Repeat the diamond step for each of the four squares now defined, using the new modified range of a*[-n, +n].  Repeat, continuing to decrease the range multiplicatively (a^(b-1)*[-n, +n], for example) until at the pixel level.  What is remaining should be a gradually changing height map that can be turned into an image or some other format.

The next step for my implementation was to convert the height map to a graph, with each node linked to its north, south, east, and west neighbors.  This makes it easier to manipulate it like a map, adding things like rivers, roads, etc., and breaks its dependence on the 2D array format.  I initially planned to implement other terrain generation algorithms, but it was a pretty low priority so I never got that far.

There is some initial work on generating rivers, but the rivers tend to fall into the fairly regularly spaced divots in the landscape caused by the diamond square algorithm's particular quirks.  I had planned to make the rivers that do so fill the divots, overflowing at the lowest point, but it was at this point that I abandoned the project for school (and other) reasons.

Once the graph is built and processed, the program passes it to yet another function that (ideally) builds a picture based on the data stored in the graph, such as heights, river nodes, ocean, etc.  The colors associated with each height are generated based percentiles; at the moment, there are four quartiles, but it is a simple matter to extend it to support more colors.

At this point, it's done.  It's generated the height map, converted that to a graph, processed the graph for various bits of information and effects, converted that to a color map, and saved it as an image.  There are several output images in the output folder in the repository, some of which have little red rivers that mostly end in the divots in the landscape.