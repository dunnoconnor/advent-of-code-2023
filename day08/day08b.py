from readfile import read_file
import re
import numpy

text = read_file("day08.data.txt");

def get_steps(t:[str]) -> int:
    moves= {}
    directions = t.pop(0);
    print(directions)
    re_codes = re.compile(r'\w+');
    for l in t:
        codes = re_codes.findall(l)
        moves[codes[0]]={'L':codes[1],'R':codes[2]};
    
    ghosts = []
    for key in moves:
        if key[2]=='A':
            ghosts.append(key)

    d_index = 0
    step_counts = []
    for g in ghosts:
        steps = 0
        while(g[2]!='Z'):
            dir = directions[d_index%len(directions)]
            d_index += 1
            g = moves[g][dir]
            steps +=1
        step_counts.append(steps)

    ghost_path = numpy.lcm.reduce(step_counts)        

    return ghost_path

print(get_steps(text))