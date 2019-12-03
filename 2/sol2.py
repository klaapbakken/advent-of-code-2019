import os

from pathlib import Path
from operator import mul

from itertools import product

from copy import deepcopy

DIR = Path(os.path.curdir)
with (DIR/"input.txt").open(mode="r") as f:
    integer_list = list(map(int, f.readline().strip().split(",")))
N = len(integer_list)

original_integer_list = deepcopy(integer_list)

integer_list[1] = 12
integer_list[2] = 2

opcodes = {
    99 : lambda x: 1/0,
    1 : lambda x: sum(x),
    2 : lambda x: mul(*x)
}

def process_chunk(i, ii, iii, iv, integer_list):
    integer_list[iv] = opcodes[i]((integer_list[ii], integer_list[iii]))

def run_integer_program(memory):
    chunks = (memory[i:i+4] for i in range(0, N, 4))
    for chunk in chunks:
        try:
            process_chunk(*chunk, memory)
        except:
            break

run_integer_program(integer_list)
print(integer_list[0])

def replace(x, y, memory):
    memory[1] = x
    memory[2] = y

for nums in product(range(100), range(100)):
    new_integer_list = deepcopy(original_integer_list)
    replace(*nums, new_integer_list)
    run_integer_program(new_integer_list)
    if new_integer_list[0] == 19690720:
        print(100*nums[0] + nums[1])
        break
    del new_integer_list

