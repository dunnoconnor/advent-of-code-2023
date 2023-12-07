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
    rank = ['2','3','4','5','6','7','8','9','T','Q','K','A'];
    count = collections.Counter(h);
    jokers = count['J'];
    count['J']=0
    high_count = count.most_common();
    highest = high_count[0][0];
    if len(high_count)>1:
        if high_count[0][1] == high_count[1][1]:
            tie_break = rank[max(rank.index(high_count[0][0]),rank.index(high_count[1][0]))];
            highest = tie_break;
    count[highest]+= jokers;
    high_count = count.most_common();
    if high_count[0][1] > 3:
        return str(high_count[0][1]+2);
    if high_count[0][1] == 3:
        if len(high_count)>1 and high_count[1][1] == 2:
            return '5';
        return '4';
    if high_count[0][1] == 2:
        if len(high_count)>1 and high_count[1][1]==2:
            return '3';
        return '2'
    else:
        return '1';

def card_valuer(c:str)-> str:
    face_list =['T','*','Q','K','A'];
    if c.isdigit():
        return '0'+c;
    if c == 'J':
        return '01';
    return str(face_list.index(c)+10);

print(get_winnings(text))