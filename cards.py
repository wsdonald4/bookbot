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
    
    def deal_four(self):
        for i in range(10):
            print(self.deal_card())

    def remaining_cards(self):
        return self.__cards
    
def main():
    player1 = DeckOfCards()
    player2 = player1
    player3 = player1
    player1.shuffle_deck()
    print("player 1's cards")
    player1.deal_four()
    print(len(player1.remaining_cards()))
    print()
    print("player 2's cards")
    player2.deal_four()
    print(len(player2.remaining_cards()))
    print()
    print("player 3's cards")
    player3.deal_four()
    print(len(player3.remaining_cards()))
    
    
main()