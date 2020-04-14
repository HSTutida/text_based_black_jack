from deck import Cards
from player import Player
import random


def game():

     lst_suits = ['Spades','Hearts','Clubs','Diamond']
     lst_values = list(range(1,14))
     deck = []

     for suit in lst_suits:
         for value in lst_values:
               deck.append((value,suit))

     #instance an object table of class Cards giving a 52 card deck as entry value         
     table = Cards(deck) 


     #print all cards
     #print('PRINT ALL CARDS')
     #print(table)
     #print('')


     #print a card of index n
     #print('print card of index 3\n')
     #print(table.print_card(3))

     #remove card from the table

     #print('remove card of index 3\n')
     #table.remove_card(table.deck[3])


     #print('print table')
     #print(table)

     print('Adding cards to player hand')
     human = Player([],10,0)
     bot = Player([],10,0)



     #Adds card to player's hand and remove the card from deck
     random_index1 = random.randint(0,len(table.deck)-1)
     human.add_card(table.print_card(random_index1))
     table.remove_card(table.deck[random_index1])

     random_index2 = random.randint(0,len(table.deck)-1)
     human.add_card(table.print_card(random_index2))
     table.remove_card(table.deck[random_index2])

     random_index1 = random.randint(0,len(table.deck)-1)
     bot.add_card(table.print_card(random_index1))
     table.remove_card(table.deck[random_index1])

     random_index2 = random.randint(0,len(table.deck)-1)
     bot.add_card(table.print_card(random_index2))
     table.remove_card(table.deck[random_index2])

     #initialize the total sum
     human.total = int(human.print_total())
     bot.total = int(bot.print_total())

     #print(table)
     #table.print_deck_table()

     print('cards remaining:')
     print(len(table.deck))
     print('')
     print('')
     print('------------GAME START-----------------')

     bot.print_total()
     print('Player hand:')
     human.print_hand()
     print('Human total: ')
     print(human.print_total())

     print('\nBot hand:')
     #bot.print_hand()
     bot.print_single_hand()
     
     #print('\nBot total:')
     #print(bot.print_total)

     #Human Turn

     while True:
          print('\n------------------------------------')
          choose = input('Player wants to bid?: (y or n)')
          print('------------------------------------')
          print('')
          if choose == 'y':
               random_index1 = random.randint(0,len(table.deck)-1)
               human.add_card(table.print_card(random_index1))
               table.remove_card(table.deck[random_index1])
            
               print('Human hand:')
               human.print_hand()
               print('Human total: ')
               print (human.print_total())
               human.total = int(human.print_total())
               
               #subtract 10 if the sum is above 21 an a A is found
               if human.total >21:
                    human.subtract_A()

               if human.total >21:
                    print('--------------Human BUST---------------')
                    print('')
                    break
          else:
               break	

     #PC TURN

     bot.total = int(bot.print_total()) #receives the total considering A = 11

     while bot.total<16 and human.total <=21:
     	
          random_index1 = random.randint(0,len(table.deck)-1)
          bot.add_card(table.print_card(random_index1)) 
          table.remove_card(table.deck[random_index1])
          bot.total = int(bot.print_total())

          if bot.total > 21:
               bot.subtract_A()

     print('Bot hand:')
     bot.print_hand()
     print('Bot total: ')
     print (bot.total)


     if bot.total>21:
          print('')
          print('***********************************')
          print('Results')
          print('***********************************')
          print('Player wins')
          print('Human total: {}'.format(human.total))
          print('PC total: {}'.format(bot.total))
          print('***********************************')
          print('Cards remaining: {}'.format(len(table.deck)))
          return True


     elif bot.total >= human.total or human.total>21:
          print('')
          print('***********************************')
          print('Results')
          print('***********************************')
          print('PC wins')
          print('Human total: {}'.format(human.total))
          print('PC total: {}'.format(bot.total))
          print('***********************************')
          print('Cards remaining: {}'.format(len(table.deck)))
          return False
     else:
          print('')
          print('***********************************')
          print('Results')
          print('***********************************')
          print('Player wins')
          print('Human total: {}'.format(human.total))
          print('PC total: {}'.format(bot.total))
          print('***********************************')
          print('Cards remaining: {}'.format(len(table.deck)))
          return True

     #table.print_deck_table()
     #print('cards remaining:')
     #print(len(table.deck))
