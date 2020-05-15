from readPuzzle import readPuzz
from backtracker import backtracker
import numpy as np
grid,val = np.array(readPuzz())
if val:
	backtracker(grid)
else:
	print("Exited")