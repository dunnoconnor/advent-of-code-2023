from parse import *
import re
from readfile import read_file

# use the digitRange to check if surrounding indexes (up, down, left, or right) contain a special character
# if so, add the number to the parts list - return the sum

text = read_file("day03.data.txt");

def sum_parts_list() -> list:
    # readfile and split by line
    parts = [];
    line=0;
    while line<len(text):
        # loop through each line, checking for digits
        re_nums = re.compile(r'\d+');
        result = re_nums.finditer(text[line]);
        for num in result:
            s = num.span();
            g = num.group()
            parts.append(is_part(line,s,g));
            print(parts)
        line+=1;
    return sum(parts)

def is_part(line,s,g):
    left = max(0,s[0]-1);
    right = min(len(text[line]),s[1]+1);
    top = max(0,line-1);
    bottom = min(len(text)-1,line+2);
    for i in range(top,bottom):
        print(text[i][left:right])
        x = re.findall("[^0-9.]", text[i][left:right]);
        if x:
            return int(g);
    return 0;

print(sum_parts_list());
