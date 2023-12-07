from readfile import read_file
from merge_sort import merge_sort
import collections

text = read_file("day07.data.txt");

def get_winnings(t:[str]) -> int:
    winnings=0;
    hands = sort_hands(t);
    for i in range(len(hands)):
        winnings += hands[i][1]*(i+1)
    return winnings;

def sort_hands(t:[str]) -> [tuple]:
    hands = []
    for line in t:
        l = line.split(" ")
        hands.append((get_hand_value(l[0]),int(l[1])))
    hands = merge_sort(hands);
    return hands;

def get_hand_value(h:str)->int:
    value = "";
    value += card_counter(h);
    for c in h:
        value += card_valuer(c)
    return int(value)

def card_counter(h:str) -> str:
    count = collections.Counter(h)
    high_count = count.most_common(2)
    if high_count[0][1] > 3:
        return str(high_count[0][1]+2);
    if high_count[0][1] == 3:
        if high_count[1][1] == 2:
            return '5';
        return '4';
    if high_count[0][1] == 2:
        if high_count[1][1]==2:
            return '3';
        return '2'
    else:
        return '1';

def card_valuer(c:str)-> str:
    face_list =['T','J','Q','K','A'];
    if c.isdigit():
        return "0"+c;
    return str(face_list.index(c)+10);

print(get_winnings(text))