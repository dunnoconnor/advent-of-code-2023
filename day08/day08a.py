from readfile import read_file
import re

text = read_file("day08.data.txt");

def get_steps(t:[str]) -> int:
    moves= {}
    directions = t.pop(0);
    print(directions)
    re_codes = re.compile(r'\w+');
    for l in t:
        codes = re_codes.findall(l)
        moves[codes[0]]={'L':codes[1],'R':codes[2]};

    curr = 'AAA'
    d_index = 0
    step_count = 0
    
    while(curr!='ZZZ'):
        dir = directions[d_index%len(directions)]
        d_index += 1
        curr = moves[curr][dir]
        print(curr)
        step_count +=1
    
    return step_count



print(get_steps(text))