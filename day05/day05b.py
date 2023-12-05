from Almanac import Almanac
from readfile import read_file
import re

text = read_file("day05.data.txt");


def get_locs(t:list) -> list:
    seed_line = t.pop(0)
    re_nums = re.compile(r'\d+');
    seed_nums = re_nums.findall(seed_line);
    seed_ids = find_seed_ids(seed_nums);
    almanac = Almanac(seed_ids);
    curr_type = "see";
    for l in t:
        if len(l)<1:
            pass
        elif l[0].isdigit():
            curr_nums = re_nums.findall(l);
            almanac.convert(curr_type,curr_nums);
        else:
            curr_type = l[0:3]
    
    almanac.set_seed_atrributes()

    return almanac.min_loc;

def find_seed_ids(nums:list) -> list:
    arr=[];
    i=0;
    while i < (len(nums)-1):
        arr.append((int(nums[i]),(int(nums[i])+int(nums[i+1]))))
        i+=2;
    return arr;


print(get_locs(text))