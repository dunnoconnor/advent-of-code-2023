from Card import Card

class Deck:
    def __init__(self):
        self.cards: list = [];
  
    def add_card(self,card:Card) -> None:
        self.cards.append(card);