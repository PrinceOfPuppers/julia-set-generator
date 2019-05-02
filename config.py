from numpy import linspace
from multiprocessing import cpu_count
class Config:
    def __init__(self):
        self.resolution=(2000,2000)

        #self.seedPoint=(-0.8 + 0.156j)
        self.seedPoint=( 0.285 + 0.01j)
        #self.seedPoint=1-1.61803398875
        #iterations and resolution are best considered togeather ie 5000x5000 needs 
        #an iteration number greather than 30
        self.iterations=1000
        self.threshold=4

        self.enableFullScreen=True

        #mutiProcessing only supported for color mandelbrot
        self.enableMultiProcessing=True

        #the number of processes spawned is determined by cpu count, change if you wish
        self.processesUsed=cpu_count()

        #starting screen (yUpperBound is calculated to keep it square)
        xLowerBound=-2
        xUpperBound=2

        yLowerBound=-2

        #after each click zoom, how big is the screen compared to last time
        self.newWindowSize=1/2

        #non adjustable
        yUpperBound=yLowerBound+(xUpperBound-xLowerBound)
        self.xInitalBounds=(xLowerBound,xUpperBound)
        self.yInitalBounds=(yLowerBound,yUpperBound)