from parse import *
import re
from readfile import read_file
from Card import Card

text = read_file("day04.data.txt");
'''
Plan:
Card class: winning_nums, your_nums, value
Card.get_wins() cound occurances of your_nums in winning_nums
Card.get_value() calculate points based on win_count
'''

def sum_values(t:str) -> int:
    re_nums = re.compile(r'\d+');
    cards=[];
    for line in t:
        line = line.split(":");
        card_num = re_nums.findall(line[0]);
        nums = line[1].split("|");
        win_nums= re_nums.findall(nums[0]);
        your_nums = re_nums.findall(nums[1]);
        # print(card_num,win_nums,your_nums);
        this_card = Card(int(card_num[0]),list(map(int,win_nums)),list(map(int,your_nums)))
        cards.append(this_card)
    return sum(c.value for c in cards)

print(sum_values(text))