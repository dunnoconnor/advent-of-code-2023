class Card:
    def __init__(self,id:int,win_nums:list,your_nums:list):
        self.id = id;
        self.win_nums = win_nums;
        self.your_nums = your_nums;
        self.wins = self.get_wins();
        self.value = self.get_value();
        self.count = 1;
  
    def get_wins(self) -> int:
        win_count = 0;
        for num in self.your_nums:
            if num in self.win_nums:
                win_count += 1;
        return win_count;

    def get_value(self):
        value = 1;
        wins_count = self.wins;
        if wins_count<=1:
            return wins_count;
        else:
            for i in range(wins_count-1):
                value = value*2;
        return value;
