# open file, read data, split by newline
f = open("day01.data.txt", "r");
text = f.read();
f.close();

numbers = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}
first_letters = "otfsen";
last_letters = "eorxnt";

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
        elif(c[p1] in first_letters and firstChar==None):
            firstChar = check_written_number("p1", p1, c);
        if(c[p2].isdigit() and lastChar==None):
            lastChar = c[p2];
        elif(c[p2] in last_letters and lastChar==None):
            lastChar = check_written_number("p2", p2, c);
        p1+=1;
        p2-=1;
    print(firstChar+lastChar)
    return int(firstChar+lastChar);

#check if the letter is part of a written number
def check_written_number(p:str, i:int, c:str) -> str:
    if(p=="p1"):
        for key, value in numbers.items():
            if(c[i:(i+len(key))]==key):
                return value;
    elif(p=="p2"):
        for key, value in numbers.items():
            if(c[i-len(key)+1:i+1]==key):
                print(key, value)
                return value;
    else:
        return None;



# call function
print(get_calibration_values(text))
