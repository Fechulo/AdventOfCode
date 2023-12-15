card_labels = "23456789TJQKA"

class Card:
	def __init__(self, label):
		self.label = label

	def __str__(self):
		return self.label

	def is_stronger_than(self, card):
		my_strength = card_labels.find(self.label)
		other_strength = card_labels.find(card.label)
		return my_strength > other_strength

class Hand:
	def __init__(self, hand, bid):
		self.bid = bid
		self.cards = []
		for char in hand:
			self.cards.append(Card(char))
		self.type = self.type()

	def type(self):
		cards_seen = []
		eigen = []
		
		for card in self.cards:
			try:
				i = cards_seen.index(card.label)
				eigen[i] += 1
			except ValueError:
				eigen.append(1)
				cards_seen.append(card.label)
		
		eigen.sort(reverse=True)

		return eigen

	def is_stronger_than(self, hand):
		my_type = self.type
		other_type = hand.type

		if len(my_type) < len(other_type):
			return True
		if len(other_type) < len(my_type):
			return False
		if my_type[0] > other_type[0]:
			return True
		if other_type[0] > my_type[0]:
			return False

		for i in range(len(self.cards)):
			my_card = self.cards[i]
			other_card = hand.cards[i]

			if my_card.is_stronger_than(other_card):
				return True
			if other_card.is_stronger_than(my_card):
				return False

		return False

data = open("input")

hands = []

for line in data:
	space = line.find(' ')
	new_hand = Hand(line[:space], int(line[space+1:]))
	if (not hands) or new_hand.is_stronger_than(hands[-1]):
		hands.append(new_hand)
	else:
		for i, hand in enumerate(hands):
			if hand.is_stronger_than(new_hand):
				hands.insert(i, new_hand)
				break

answer = 0

for i, hand in enumerate(hands):
	answer += (i+1) * hand.bid

print(answer)