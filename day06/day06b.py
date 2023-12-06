
from readfile import read_file
import re
from math import sqrt, floor, ceil, prod

text = read_file("day06.data.txt");

def get_possible_wins(t:list) -> list:
    t_line = t[0];
    d_line = t[1];
    re_nums = re.compile(r'\d+');
    time = "".join(re_nums.findall(t_line));
    distance = "".join(re_nums.findall(d_line));
    print(time,distance)
    wins = get_races(int(time),int(distance));
    return int(wins);


def get_races(time:int,dist:int) -> int:
    # translating inputs for quadratic formula
    a = -1;
    b= time;
    c = -dist;
    low_bound, high_boundary = quadratic(a,b,c);
    wins = high_boundary - low_bound;
    return wins;

def quadratic(a:int,b:int,c:int) ->(int,int):
    first  = (-b + sqrt(b*b-4*a*c)) / (2*a);
    second = (-b - sqrt(b*b-4*a*c)) / (2*a)-1;
    return (floor(first),ceil(second))

print(get_possible_wins(text))