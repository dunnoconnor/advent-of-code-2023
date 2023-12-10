from readfile import read_file
from itertools import pairwise

text = read_file("day09.data.txt");

def get_sum_of_expected(t:[str]) -> int:
    sum_e = 0
    for l in t:
        sum_e += get_expected(l)
    return sum_e

def get_expected(l:[str]) -> int:
    nums = l.split(" ")
    nums = list(map(int, nums))
    layers = [nums]
    while not all(n == 0 for n in layers[-1]):
        layers.append(get_layer(layers[-1]))
    if len(layers)>1:
        layers = generate_next(layers)
    return layers[0][-1]

def get_layer(nums:[int])->list:
    pairs = pairwise(nums)
    down = []
    for p in pairs:
        down.append(p[1]-p[0])
    return down

def generate_next(l:list) -> list:
    for i in range(1,len(l)):
        print(l,i)
        diff = l[-i][-1]
        last = l[-(i+1)][-1]
        l[-(i+1)].append(diff+last)
    return l


print(get_sum_of_expected(text))