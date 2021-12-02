file = open(__file__[:-2]+"txt", "r")
input = file.readlines()

print(sum(int(i.split()[1]) for i in input if i.split()[0] == "forward") * sum(int(i.split()[1]) * (-1 if i.split()[0] == "up" else 1) for i in input if i.split()[0] != "forward"))

aim = 0
distance = 0
depth = 0
for i in input:
    if i.split()[0] == "forward":
        distance += (value:=int(i.split()[1]))
        depth += value * aim
    if i.split()[0] != "forward":
        aim += int(i.split()[1]) * (-1 if i.split()[0] == "up" else 1)
print(distance * depth)

import numpy as np
from functools import reduce

print((output:=reduce((lambda x, y: np.add(x, [int(y.split()[1]) * ((-1 if y.split()[0] == "up" else 1) if y.split()[0] != "forward" else 0)] + ([int(y.split()[1]),x[0]*int(y.split()[1])] if y.split()[0] == "forward" else [0,0]))), input, [0,0,0]))[1]*output[2])