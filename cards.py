import random

class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck()
    
    def create_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.__cards.append((rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if len(self.__cards) == 0:
            return None
        return self.__cards.pop()
    
    def deal_two(self):
        for i in range(2):
            print(self.deal_card())

    def remaining_cards(self):
        return self.__cards
    
    def deal_three(self):
        for i in range(3):
            print(self.deal_card())
    
def main():
    player1 = DeckOfCards()
    player2 = player1
    player3 = player1
    river = player1
    player1.shuffle_deck()
    print("player 1's cards")
    player1.deal_two()
    
    print()
    print("player 2's cards")
    player2.deal_two()
    
    print()
    print("player 3's cards")
    player3.deal_two()
    
    print()
    river.deal_three()
    print(river.deal_card())
    print(river.deal_card())

    
    
main()