from parse import *
import re
from readfile import read_file
from Card import Card
from Deck import Deck

text = read_file("day04.sample.txt");
cards = []

def count_cards(t:str) -> int:
    re_nums = re.compile(r'\d+');
    unique_cards = {};
    deck = Deck();

    for line in t:
        line = line.split(":");
        card_num = re_nums.findall(line[0]);
        nums = line[1].split("|");
        win_nums= re_nums.findall(nums[0]);
        your_nums = re_nums.findall(nums[1]);
        # print(card_num,win_nums,your_nums);
        this_card = Card(int(card_num[0]),list(map(int,win_nums)),list(map(int,your_nums)));
        unique_cards[this_card.id]=this_card;
        deck.add_card(this_card);
    
    for key in unique_cards:
        c:Card = unique_cards[key];
        for i in range(1,c.wins):
            deck.add_card(unique_cards[c.id+i]);
    return len(deck.cards);

print(count_cards(text))
