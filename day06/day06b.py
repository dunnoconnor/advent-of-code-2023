
from readfile import read_file
import re
import numpy

text = read_file("day06.data.txt");

def get_possible_wins(t:list) -> list:
    t_line = t[0];
    d_line = t[1];
    re_nums = re.compile(r'\d+');
    time = "".join(re_nums.findall(t_line));
    distance = "".join(re_nums.findall(d_line));
    print(time,distance)
    wins = get_races(int(time),int(distance));
    return wins;

def get_races(t:int,d:int):
    wins =0;
    for i in range(1,t):
        race = (t-i)*i;
        if race>d:
            wins+=1;
    return wins;

print(get_possible_wins(text))