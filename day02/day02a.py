from parse import *
# split line into id value, r val, g val, b val
# if r,g,and b all below limits - add id to sum
# return sum

# open file, read data, split by newline
f = open("day02.data.txt", "r");
text = f.read();
f.close();

# store max values for each color
limits = {"red":12,"green":13,"blue":14};

def get_possible_games(text:str) -> int:
    id_total = 0;
    lines = text.split("\n")
    # split line into id value, r val, g val, b val
    for l in lines:
        l = l.split(":");
        game = l.pop(0);
        game = parse('Game {:d}', game)[0];
        rounds = l[0].split(";");
        id_total += check_game(game,rounds);
        print(game, id_total)

    return id_total;

def check_game(game:int, rounds:list) -> int:
    for pull in rounds:
        pull = pull.split(",");
        for die in pull:
            die = die.strip();
            p = parse('{:d} {:w}', die)
            num=p[0]
            color=p[1]
            if(num>limits[color]):
                print(num, color, " is too many")
                return 0;
    return game;

print(get_possible_games(text));