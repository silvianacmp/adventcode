import numpy as np
import re

grid = np.zeros((1000, 1000))
on = re.compile('turn on.*')
off = re.compile('turn off.*')
toggle = re.compile('toggle.*')

while True:
    line = raw_input()
    if line == "end":
        break

    # find the grid indices in the given instruction
    limits = re.findall('\\d+', line)
    limits = [int(x) for x in limits]
    if on.match(line):
        grid[limits[0]:limits[2] + 1, limits[1]:limits[3] + 1] = 1
    elif off.match(line):
        grid[limits[0]:limits[2] + 1, limits[1]:limits[3] + 1] = 0
    else:
        grid[limits[0]:limits[2] + 1, limits[1]:limits[3] + 1] = 1 - grid[limits[0]:limits[2] + 1,
                                                                     limits[1]:limits[3] + 1]

print np.sum(grid)



