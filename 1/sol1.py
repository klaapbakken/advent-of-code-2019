from pathlib import Path
import os
from math import floor

DIR = Path(os.path.curdir)
input_list = []
with (DIR/"input.txt").open(mode="r") as f:
    while True:
        l = f.readline().strip()
        if len(l) == 0:
            break
        input_list.append(l)

input_list = list(map(int, input_list))

def calculate_fuel(mass):
    return floor(mass/3) - 2

print(f"Required total fuel: {sum(map(calculate_fuel, input_list))}")

def calculate_fuels_fuel(mass, total=0):
    fuel = calculate_fuel(mass)
    if fuel < 0:
        return total
    else:
        total += fuel
        return calculate_fuels_fuel(fuel, total=total)

print(f"Required total fuels fuel: {sum(map(calculate_fuels_fuel, input_list))}")
    
        


