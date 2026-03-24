from Deck import Deck

class PokerHand:
    def __init__(self):
        """
        Create a brand-new deck, shuffle it and deal 5 cards
        """
        deck = Deck() #create a new deck
        deck.shuffle() # shuffle the deck
        self._cards = [] # create an empty hand
        for _ in range(5): # we deal 5 cards!!
            self._cards.append(deck.deal()) # add a card to the hand, until 5

    @property
    def cards(self):
        return tuple(self._cards)

    def __str__(self):
        return str(self._cards)

hand = PokerHand()
print(hand)

