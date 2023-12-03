from parse import *
# split line into id value, r val, g val, b val
# get each lines max r,g,&b values - multiply these together (called power)
# return sum of all powers

# open file, read data, split by newline
f = open("day02.data.txt", "r");
text = f.read();
f.close();

def get_power_of_games(text:str) -> int:
    pow_total = 0;
    lines = text.split("\n")
    # split line into id value, r val, g val, b val
    for l in lines:
        l = l.split(":");
        game = l.pop(0);
        rounds = l[0].split(";");
        pow_total += check_game_pow(rounds);
        print(pow_total);

    return pow_total;

def check_game_pow(rounds:list) -> int:
    # store max values for each color
    max = {"red":0,"green":0,"blue":0};
    for pull in rounds:
        pull = pull.split(",");
        for die in pull:
            die = die.strip();
            p = parse('{:d} {:w}', die);
            num=p[0];
            color=p[1];
            if(num>max[color]):
                max[color]=num;
    print(max["red"],max["green"],max["blue"])
    power = max["red"]*max["green"]*max["blue"]
    return power;

print(get_power_of_games(text));