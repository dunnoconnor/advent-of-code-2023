def read_file(name):
    f = open(name, "r");
    text = f.read();
    f.close();
    return text.split("\n")