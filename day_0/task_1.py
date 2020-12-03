from itertools import permutations 

def input_list():
    with open('day_0/input.txt') as f:
        content=f.readlines()
        return [int(line.strip()) for line in content]


def solution(parsed_list=input_list()):
    perms=permutations(parsed_list,3)
    for a,b in perms:
        if a+b== 2020:
            return a*b
print(solution())
