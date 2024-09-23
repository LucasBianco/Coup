import random


class Player:

    def __init__(self, name, card1, card2, coins = 0):
        self.__name = name
        self.__card1 = card1
        self.__card2 = card2
        self.__coins = coins
        self.__numcards = 2

    def get_card1(self):
        return self.__card1
    
    def get_card2(self):
        return self.__card2


    def changecard(self, newcard1, newcard2 = 'none'):
        self.__card1 = newcard1
        self.__card2 = newcard2


    def alive(self):
        if self.__card1 == 'none':
            return False
        else:
            return True

    def delete_card(self):
        
        self.__numcards -= 1
        if self.__numcards == 1:
            print(f'{self}')
            if (n:= int(input("Choose 1 or 2: "))) == 1:
                self.__card1 = self.__card2
                self.__card2 = "none"
            else:
                self.__card2 = 'none'

        else:
            
            self.__card1 = 'none'
        print(self)

    def __str__(self):
        return f'{self.__name}: {self.__card1} card 1 and {self.__card2} card 2'
    
    def check_contest(self, card):
        if card != self.__card1 and card != self.__card2:
            print("Your dispute is right.")
            self.delete_card()
            return True
        else:
            print("Your dispute is wrong.")
            return False


    def add_coins(self, coins):
        self.__coins += coins

    def substract_coins(self, coins):
        self.__coins -= coins

    def display_coins(self):
        print(self.__coins)

    def get_coins(self):
        return self.__coins

    def display_name(self):
        return (self.__name)
    
    def randomly_change_cards(self, card_to_change, deck_cards):
        # print(deck_cards)
        print()

        if self.__card1 == card_to_change:
            self.__card1 = random.choice(deck_cards)
            deck_cards.remove(self.__card1)
            deck_cards.append(card_to_change)
        else:
            self.__card2 = random.choice(deck_cards)
            deck_cards.remove(self.__card2)
            deck_cards.append(card_to_change)

        print(self.display_name())
        print(self)
        print()

    def cards_quantity(self):
        if self.__card2 == 'none':
            return 1
        else:
            return 2
        
    def display_cards(self, card3, card4):
        if self.__card2 == 'none':
            print(f'Card 1 - {self.__card1}; Card 2 - {card3}; Card 3 - {card4}')
        else:
            print(f'Card 1 - {self.__card1}; Card 2 - {self.__card2}; Card 3 - {card3}; Card 4 - {card4}')


        

'''
Player1 = Player("Duke", "Assassin")
Duke_add_3_coins(Player1)
Player1.display_coins()'''