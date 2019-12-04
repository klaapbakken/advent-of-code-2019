import sys
from itertools import chain
from itertools import product

input_string = sys.argv[1]

input_tuple = tuple(map(int, input_string.split("-")))

def rule_1(number):
    return any(map(lambda x: x[0] == x[1], [(i, j) for i, j in zip(number[:-1], number[1:])]))
    
def rule_2(number):
    previous_digit = number[0]
    for digit in number[1:]:
        if digit >= previous_digit:
            previous_digit = digit
            continue
        else:
            return False
    return True

#Not needed? At least not for my input
# -----------
def rule_3(number):
    return len(number) == 6

def rule_4(number):
    return input_tuple[0] <= int(number) <= input_tuple[1]
#-----------

counter = 0
for number in map(str, range(input_tuple[0], input_tuple[1] + 1)):
    if all(map(lambda x: x(number), [rule_1, rule_2, rule_3, rule_4])):
        counter += 1
print(counter)

def n_matching(n, number):
    matching = []
    i = 0
    positions = tuple(range(i, n+i))
    while positions[-1] < len(number):
        subsequence = list(map(number.__getitem__, positions))
        for digit in range(10):
            if all(map(lambda x: x == str(digit), subsequence)):
                matching.append(positions)
        i += 1
        positions = tuple(range(i, n+i))
    return matching

def altered_rule_1(number):
    two_matching_positions = []
    for i_position, i in enumerate(number[:-1]):
        j_position = i_position + 1
        j = number[j_position]
        if i == j:
            two_matching_positions.append((i_position, j_position))

    #If there is no repeated digits, return False
    if len(two_matching_positions) == 0:
        return False

    n_matching_positions = list(chain(*map(lambda x: n_matching(x, number), [3, 4, 5, 6])))

    #If there are repeated digits of length two, but not of length three, return True.
    if len(n_matching_positions) == 0:
        return True
    
    for two_pos in two_matching_positions:
        allowed = True
        for n_pos in n_matching_positions:
            coincides = set(two_pos) <= set(n_pos)
            if coincides:
                allowed = False
                break
        if allowed:
            return True

counter = 0
for number in map(str, range(input_tuple[0], input_tuple[1] + 1)):
    if all(map(lambda x: x(number), [altered_rule_1, rule_2, rule_3, rule_4])):
        counter += 1
print(counter)