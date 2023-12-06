
from readfile import read_file
import re
import numpy

text = read_file("day06.data.txt");

def get_possible_wins(t:list) -> list:
    t_line = t[0];
    d_line = t[1];
    re_nums = re.compile(r'\d+');
    times = re_nums.findall(t_line);
    distances = re_nums.findall(d_line);
    win_list =[];
    for i in range(len(times)):
        win_list.append(get_races(int(times[i]),int(distances[i])));
    return numpy.prod(win_list);
def get_races(t:int,d:int):
    wins =0;
    for i in range(1,t):
        race = (t-i)*i;
        if race>d:
            wins+=1;
    return wins;

print(get_possible_wins(text))