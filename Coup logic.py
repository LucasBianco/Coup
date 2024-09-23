import random
from Coup_player import Player
import time


def check_if_alive(list_player, alives):
    # print(alives)
    for (index,key) in enumerate(list_player):
        if key != 'none':
            if not key.alive():
                list_player[index] = 'none'
                
                alives -= 1
    return alives





def Take_1_coin(Player):
    Player.add_coins(1)

def Take_2_coins(Player, contested = False):
    if not contested:
        Player.add_coins(2)


def Action_take_1_coin(i):
    Take_1_coin(list_players[i])
    print(f'{list_players[i].display_name()} coin(s): ')
    list_players[i].display_coins()

def Action_take_2_coins(i):
    print("If you are a duke, you can block it.")
            
    blocked = False
    player_who_blocked = input("If you want to block it, write your name. Otherwise, just press space: ")
    print()
    if player_who_blocked != ' ':
        contested = input(f"If you want to dispute it that {player_who_blocked} has a Duke, write your name. Otherwise, just press space: ")
        if contested != ' ':
            dispute = list_players[find_player[player_who_blocked]].check_contest("Duke")
            if dispute:
                blocked = False
            else:
                blocked = True
                list_players[find_player[contested]].delete_card()
                list_players[find_player[player_who_blocked]].randomly_change_cards("Duke",cards)

    else:
        blocked = False


    Take_2_coins(list_players[i], blocked)
    print(f'{list_players[i].display_name()} coin(s): ')
    list_players[i].display_coins()



def Duke_add_3_coins(Player, contested = False):
    if not contested:
        Player.add_coins(3)

def Action_Duke_3_coins(i):

    blocked = False
    contested = input(f"If you want to dispute that {list_players[i].display_name()} has a Duke, write your name. Otherwise, just press space: ")
    if contested != ' ':
        dispute = list_players[i].check_contest("Duke")
        if dispute:
            blocked = True
        else:
            blocked = False                        
            list_players[find_player[contested]].delete_card()
            list_players[i].randomly_change_cards("Duke",cards)
            # print(cards)
        
    Duke_add_3_coins(list_players[i], blocked)
    print(f'{list_players[i].display_name()} coin(s): ')
    list_players[i].display_coins()



def Capitain_steal_2_coins(Player_capitain, Player_victim, contested = True):

    if not contested:
        if Player_victim.get_coins() == 0:
            Player_capitain.add_coins(0)
            Player_victim.substract_coins(0)
        elif Player_victim.get_coins() == 1:
            Player_capitain.add_coins(1)
            Player_victim.substract_coins(1)
        else:
            Player_capitain.add_coins(2)
            Player_victim.substract_coins(2)
    print(f'{Player_capitain.display_name()} coin(s): ')
    Player_capitain.display_coins()
    print()
    print(f'{Player_victim.display_name()} coin(s): ')
    Player_victim.display_coins()

def Action_Capitain_steal(i):
    victim_player = find_player[input("Who do you want to steal from: ")]
    victim_player = list_players[victim_player]
    blocked = False
    contested = input(f"If you want to dispute that {list_players[i].display_name()} has a Capitai, write your name. Otherwise, just press space: ")
    if contested != ' ':
        dispute = list_players[i].check_contest("Capitain")
        if dispute:
            blocked = True
        else:
            blocked = False                        
            list_players[find_player[contested]].delete_card()
            list_players[i].randomly_change_cards("Capitain",cards)
    else:
        print(f"What's your action {victim_player.display_name()}: \n"
        "1 - I'm capitain I will block that.\n"
          "2 - I'm ambassador I will block that.\n"
          "3 - Nothing I will accept that steal.\n")
    
        action = int(input("Type your action: "))

        if action == 1:

            contested = input(f"If you want to dispute that {victim_player.display_name()} has a Capitain, write your name. Otherwise, just press space: ")
            if contested != ' ':
                dispute = victim_player.check_contest("Capitain")
                if not dispute:
                    list_players[i].delete_card()
                    blocked = True
                    victim_player.randomly_change_cards("Capitain",cards)
            else:
                blocked = True

        elif action == 2:

            contested = input(f"If you want to dispute that {victim_player.display_name()} has an Ambassador, write your name. Otherwise, just press space: ")
            if contested != ' ':
                dispute = victim_player.check_contest("Ambassador")
                if not dispute:
                    list_players[i].delete_card()
                    blocked = True
                    victim_player.randomly_change_cards("Ambassador",cards)

            else:
                blocked = True

     

    Capitain_steal_2_coins(list_players[i], victim_player, blocked)



def Ambassador_cards(Player_Ambassador, blocked, cards):
    
    
    if not blocked:
        # print(cards)
        card3 = random.choice(cards)
        cards.remove(card3)
        card4 = random.choice(cards)
        cards.remove(card4)
        # print(cards)
        Player_Ambassador.display_cards(card3, card4)
        if Player_Ambassador.cards_quantity() == 1:
            hand = [Player_Ambassador.get_card1(), card3, card4]
            newcard = int(input("Select the number of the card that you want: "))
            Player_Ambassador.changecard(hand[newcard - 1])
            hand.pop(newcard - 1)
        else:
            hand = [Player_Ambassador.get_card1(), Player_Ambassador.get_card2(), card3, card4]
            newcard1 = int(input("Select the number of the first card that you want: "))
            newcard2 = int(input("Select the number of the second  card that you want: "))
            Player_Ambassador.changecard(hand[newcard1 - 1], hand[newcard2 - 1])
            
            hand.pop(newcard1 - 1)
            hand.pop(newcard2 - 2)

        for i in hand:
            cards.append(i)

        # print(cards)
        print()
        print(Player_Ambassador)

def Action_Ambassador_cards(i):
    blocked = False
    contested = input(f"If you want to dispute that {list_players[i].display_name()} has an Ambassador, write your name. Otherwise, just press space: ")
    if contested != ' ':
        dispute = list_players[i].check_contest('Ambassador')
        if dispute:
            blocked = True
        else:
            list_players[find_player[contested]].delete_card()
            list_players[i].randomly_change_cards("Ambassador", cards)

    Ambassador_cards(list_players[i], blocked, cards)




def Assassin_kill(Player_victim, contested = False):
    if not contested:
        Player_victim.delete_card()

def Action_assassin_kill(i):
    list_players[i].substract_coins(3)
    victim_player = find_player[input("Who do you want to kill: ")]
    victim_player = list_players[victim_player]
    blocked = False
    contested = input(f"If you want to dispute That {list_players[i].display_name()} has an Assassin, write your name. Otherwise, just press space: ")
    if contested != ' ':
        dispute = list_players[i].check_contest("Assassin")
        if dispute:
            blocked = True
        else:
            blocked = False                        
            list_players[find_player[contested]].delete_card()
            list_players[i].randomly_change_cards("Assassin",cards)

    else:
        print(f"{victim_player.display_name()} what are you going to do:\n"
              "1 - I'm Condessa, I will block you.\n"
              "2 - Just let he kill me.")
        action = int(input("Type your action: \n"))

        if action == 1:
            contested = input(f"If you want to dispute that {victim_player.display_name()} has a Contessa, write your name. Otherwise, just press space: ")
            if contested != ' ':
                dispute = victim_player.check_contest("Contessa")
                if not dispute:
                    list_players[i].delete_card()
                    blocked = True
                    victim_player.randomly_change_cards("Contessa",cards)
                    
            else:
                blocked = True

    
    Assassin_kill(victim_player, blocked)

    print(f'{list_players[i].display_name()} coin(s): ')
    list_players[i].display_coins()



def Action_coup_7_coins(i):
    list_players[i].substract_coins(7)
    victim_player = find_player[input("Who do you want to coup: ")]
    list_players[victim_player].delete_card()






#Defining the name of the characters
Player1 = input('Type your name: ')
Player2 = input('Type your name: ')
Player3 = input('Type your name: ')
Player4 = input('Type your name: ')
Player5 = input('Type your name: ')

find_player = {Player1: 0, Player2: 1, Player3: 2, Player4: 3, Player5: 4}

Player1Cards = ['','']
Player2Cards = ['','']
Player3Cards = ['','']
Player4Cards = ['','']
Player5Cards = ['','']


cards =  ["Capitain","Capitain","Capitain","Duke","Duke","Duke","Assassin","Assassin","Assassin"
          ,"Contessa","Contessa","Contessa","Ambassador","Ambassador","Ambassador"]


for i in range(0,5*2):
    n = random.choice(cards)
    # print(n)
    if i <= 1:
        
        Player1Cards[i] = n
     
    elif i <= 3:
        i -= 2
        Player2Cards[i] = n
      
    elif i <= 5:
        i -= 4
        Player3Cards[i] = n
       
    elif i <= 7:
        i -= 6
        Player4Cards[i] = n
       
    elif i <= 9:
        i -= 8
        Player5Cards[i] = n
        
    cards.remove(n)

P1 = Player(Player1,Player1Cards[0], Player1Cards[1])
P2 = Player(Player2,Player2Cards[0], Player2Cards[1])
P3 = Player(Player3,Player3Cards[0], Player3Cards[1])
P4 = Player(Player4,Player4Cards[0], Player4Cards[1])
P5 = Player(Player5,Player5Cards[0], Player5Cards[1])
list_players = [P1, P2, P3, P4, P5]


alives = 5
k = random.randint(0,4)


while alives > 1:


    for i in range(5):


        blocked = False

        print()
        if i + k < 5:
            if list_players[k + i] == 'none':
                print('Jumped, he is dead!')
                continue
            print(f"your turn {list_players[k + i].display_name()}\n")
            

            i += k 
        else:
            if list_players[k + i - 5] == 'none':
                print('Jumped, he is dead!')
                continue
            print(f'your turn {list_players[k + i - 5].display_name()}\n')
            i += k - 5

        print(f'{list_players[i].display_name()} coin(s): ')   
        list_players[i].display_coins()
        print(list_players[i],'\n')
        print("What's your action?\n"
              "1 - Get one coin (1 coin, no one will block you)\n"
              "2 - Get extra help (2 Coins - Duke can block you)\n"
              "3 - I'm duke, I will get 3 coins\n"
              "4 - I'm capitain, I will steal from someone (2 coins - Capitains and Ambassadors can block)\n"
              "5 - I'm Ambassador, I will draw 2 more cards.")
        if list_players[i].get_coins() >= 3:
            print("6 - I'm assassin, I will pay 3 coins and kill someone (Condessa can block)")
        if list_players[i].get_coins() >= 7:
            print("7 - I will pay 7 coins and kill someone (No one can block)")
        print()
 
        action = int(input("Type here your action: "))

        if action == 1:

            Action_take_1_coin(i)

        elif action == 2:
            
            Action_take_2_coins(i)


        elif action == 3:

            Action_Duke_3_coins(i)

        elif action == 4:

            Action_Capitain_steal(i)

        elif action == 5:

            Action_Ambassador_cards(i)
        
        elif action == 6:

            Action_assassin_kill(i)

        elif action == 7:
            
            Action_coup_7_coins(i)

        print()
        alives = check_if_alive(list_players, alives)

        print(list_players)

        
for i in list_players:
    if i != 'none':
        print()
        print(f'{i.display_name()} wins!')
        

