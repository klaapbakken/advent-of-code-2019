import os
import re

from pathlib import Path

import numpy as np

DIR = Path(os.path.curdir)
with (DIR/"input.txt").open(mode="r") as f:
    first_wire = f.readline().strip().split(",")
    second_wire = f.readline().strip().split(",")
    
movement_dict = {
    "R" : lambda x, y: (x + 1, y),
    "L" : lambda x, y: (x - 1, y),
    "U" : lambda x, y: (x, y + 1),
    "D" : lambda x, y: (x, y - 1)
}
    
def process_wire(wire):
    grid_set = set()
    steps_dict = dict()
    i = j = n = 0
    for movement in wire:
        direction = movement[0]
        distance = int(movement[1:])
        for _ in range(distance):
            i, j = movement_dict[direction](i, j)
            n += 1
            if (i, j) not in steps_dict:
                steps_dict[(i, j)] = n
            grid_set.add((i, j))
    return grid_set, steps_dict

first_grid_set, first_steps_dict = process_wire(first_wire)
second_grid_set, second_steps_dict = process_wire(second_wire)
intersections = first_grid_set.intersection(second_grid_set)

def distance(z):
    x, y = z
    return abs(x) + abs(y)

distances = list(map(distance, intersections))
print(min(distances))

def steps(intersection):
    return first_steps_dict[intersection] + second_steps_dict[intersection]

print(min(map(steps, intersections)))
