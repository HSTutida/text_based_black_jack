from main import game
from player import Player

if __name__ == "__main__":
	print("run.py is being run directly")
else:
	print("run.py is being imported into another module")

#instantiating another objects to save the money
human_money = Player([],30,0)
bot_money = Player([],30,0)

while human_money.credits > 0 and bot_money.credits > 0:
	bid = int(input("\n\nDigit your bid:"))
	if game(): #if human wins

		print('\n------------Credits------------------')
		human_money.credits +=bid
		bot_money.credits -=bid

		print('Human credits {}'.format(human_money.credits))
		print('PC credits {}'.format(bot_money.credits))
		print('--------------------------------------')
		wait = input("-------------PRESS ENTER TO CONTINUE TO NEXT ROUND------------------------.")
		print('\n\n\n\n\n----------------------STARTING A NEW ROUND---------------------')

	else: #if pc wins
		print('\n------------Credits------------------')
		human_money.credits -=bid
		bot_money.credits +=bid
		print('Human credits {}'.format(human_money.credits))
		print('PC credits {}'.format(bot_money.credits))
		print('--------------------------------------')
		wait = input("-------------PRESS ENTER TO CONTINUE TO NEXT ROUND------------------------.")
		print('\n\n\n\n\n----------------------STARTING A NEW ROUND---------------------')

if human_money.credits > bot_money.credits:
	print('\n\n\n----------------------PLAYER WINS!-----------------------------')
else:
	print('\n\n\n----------------------PC WINS!-----------------------------')
