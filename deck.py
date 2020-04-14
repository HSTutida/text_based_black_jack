#Hold all the cards in game

class Cards():


    def __init__(self,deck):
        print('Deck created')   
        self.deck = deck  
    
    def __str__(self):
        return "{}".format(self.deck)
     

    #function to print a card 0 to 51        
    def print_card(self,index):
        value = self.deck[index][0]
        suit =  self.deck[index][1]
        return '{}, {}'.format(value,suit)

    def remove_card(self, card_tuple):
        print('Removing card: {}'.format(card_tuple))
        self.deck.remove(card_tuple)        


    def print_deck_table(self):
        print('Spades')
        for card in self.deck:
            if card[1] == 'Spades':
                print(card)
        print('Hearts')
        for card in self.deck:
            if card[1] == 'Hearts':
                print(card)
        print('Clubs')
        for card in self.deck:
            if card[1] == 'Clubs':
                print(card)
        print('Diamond')
        for card in self.deck:
            if card[1] == 'Diamond':
                print(card)





