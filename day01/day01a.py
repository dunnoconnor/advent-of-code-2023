# open file, read data, split by newline
f = open("day01.data.txt", "r");
text = f.read();
f.close();

# loop through text, getting command value for each line and adding to sum
def get_calibration_values(text:str) -> list:
    commands = text.split("\n");
    sum = 0;
    for c in commands:
        sum += get_calibration_value(c)
    return sum;

# get command value for this line
def get_calibration_value(c:str) -> int:
    firstChar=None;
    lastChar=None;
    # two pointers, one at the first index and one at the last
    p1 = 0;
    p2 = (len(c)-1);
    #loop through until both digits are found
    while(firstChar == None or lastChar == None):
        if(c[p1].isdigit() and firstChar==None):
            firstChar = c[p1];
        if(c[p2].isdigit() and lastChar==None):
            lastChar = c[p2];
        p1+=1;
        p2-=1;
    return int(firstChar+lastChar);

# call function
print(get_calibration_values(text))
