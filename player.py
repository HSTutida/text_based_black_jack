class Player():

	#store all player cards
	

	#store player credits
	

	def __init__(self, hand_cards, credits,total):
		#print('Player Created')
		#hand_cards format: [(int, string)], int is value, string is suit
		self.hand_cards = hand_cards
		self.total = total #saves the sum of cards 
		self.credits = credits
			

	#add cards to player hand
	#receives a string in the format 'string_number, string_suit'	
	#append in the format of tuple in the deck (int, string)
	def add_card (self,card_string):
		
		card_number = card_string.partition(',')[0]
		card_suit = card_string.split()[1] 

		card_tuple = tuple((int(card_number),card_suit))
		self.hand_cards.append(card_tuple)

	#print cards on screen, if value is above 10, convert to the letter J,K or Q equivalent	
	#if value is 1, print A
	def print_hand(self):
		for i in range(0,len(self.hand_cards)):
			if self.hand_cards[i][0] == 11:
				print("(J, {})".format(self.hand_cards[i][1]))
			elif self.hand_cards[i][0] == 12:
				print("(Q, {})".format(self.hand_cards[i][1]))
			elif self.hand_cards[i][0] == 13:	
				print("(K, {})".format(self.hand_cards[i][1]))
			elif self.hand_cards[i][0] == 1:	
				print("(A, {})".format(self.hand_cards[i][1]))
			
			else: 
				print (self.hand_cards[i])
		print('')

	#sum the total and treat the cards J,Q and K as 10
	#treat an A as a 11
	def print_total(self):
		total = 0
		for i in range(0, len(self.hand_cards)):
			if self.hand_cards[i][0] >= 11:
				total =  total + 10
			elif self.hand_cards[i][0] == 1:
				total =  total + 11
			else:
				total = total + self.hand_cards[i][0]
		return '{}'.format(total)

	def print_single_hand(self):
			if self.hand_cards[0][0] == 11:
				print("(J, {})".format(self.hand_cards[0][1]))
			elif self.hand_cards[0][0] == 12:
				print("(Q, {})".format(self.hand_cards[0][1]))
			elif self.hand_cards[0][0] == 13:	
				print("(K, {})".format(self.hand_cards[0][1]))
			elif self.hand_cards[0][0] == 1:	
				print("(A, {})".format(self.hand_cards[0][1]))
			
			else: 
				print (self.hand_cards[0])
			print('')

		#the total and check a deck card and if it is found an A,
		#substract 10 to the total, then exit if the sum is above 21
		#if not, continue
	def subtract_A(self):
		for i in range(0, len(self.hand_cards)):
			if self.hand_cards[i][0] == 1:
				self.total -= 10
				#print new total 
				print('New Total:')
				print(self.total)
				
				if self.total <=21:
					break

					

