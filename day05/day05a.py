from Almanac import Almanac
from readfile import read_file
import re

text = read_file("day05.data.txt");


def get_locs(t:list) -> list:
    seed_line = t.pop(0)
    re_nums = re.compile(r'\d+');
    seed_ids = re_nums.findall(seed_line);
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

    locs = []
    for s in almanac.seed_list:
        print("seed: ",s.see," soil:", s.soi, " fertilizer: ", s.fer, " water: ",s.wat, " light: ", s.lig, " temperature: ", s.tem, " humidity: ", s.hum, " location: ", s.loc);
        locs.append(s.loc)
    
    return min(locs)


print(get_locs(text))