class Pipe_Map:
    
    def __init__(self, t:int)->None:
        self.key = {
        'S':'*',
        '|':'NS',
        '-':'EW',
        'L':'NE',
        'J':'NW',
        '7':'SW',
        'F':'SE',
        '.':''
    }
        self.pos = (0,0)
        self.map = self.get_map(t)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.steps = self.get_steps()

    def get_map(self,t:[str])->[[str]]:
        pipes = []
        for i in range(len(t)):
            pipes.append([])
            for j in range(len(t[i])):
                this = t[i][j]
                if t[i][j] == 'S':
                    self.pos = (j,i)
                pipes[i].append(self.key[this])
        print(pipes)
        return pipes
    
    def get_steps(self)->int:
        count = 0
        self.x+=1
        current_pipe = self.map[self.y][self.x].replace("W", "")
        print(current_pipe)
        while current_pipe != '*':
            count += 1
            current_pipe = self.make_step(current_pipe)
        return count
        

    def make_step(self, dir:str)->str:
        print(dir)
        next = ""
        if(dir=='N'):
            self.y-=1
            next = self.map[self.y][self.x].replace("S", "")
        elif(dir=='E'):
            self.x+=1
            next = self.map[self.y][self.x].replace("W", "")            
        elif(dir=='S'):
            self.y+=1
            next = self.map[self.y][self.x].replace("N", "")            
        elif(dir=='W'):
            self.x-=1
            next = self.map[self.y][self.x].replace("E", "")            
        return next
    