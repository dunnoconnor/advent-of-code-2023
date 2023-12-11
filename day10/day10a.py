from readfile import read_file
from pipe_map import Pipe_Map
text = read_file("day10.data.txt");

'''
plan:
create key
convert grid to grid of strings with positional connections
get the x,y position of start
create step counter
check for adjacent connections to start
choose one and step
step to next until returned to S
divide step count by two, rounding up
'''

def get_farthest_pipe(text:[str]):
    pipe_map = Pipe_Map(text)
    return pipe_map.steps//2+1

print(get_farthest_pipe(text))