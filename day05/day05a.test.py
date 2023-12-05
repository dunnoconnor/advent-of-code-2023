# from day05a import sum_values
from readfile import read_file
from Almanac import Almanac
from Seed import Seed
from Converter import Converter
from day05a import get_locs
import re

text = read_file("day05.data.txt");

def test_loc_sum():
    get_locs(text)

if __name__ == "__main__":
    test_loc_sum()
    print("Everything passed")