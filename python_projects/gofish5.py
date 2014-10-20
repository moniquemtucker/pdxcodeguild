import random

#List of all cards....creates dictionary with keys 1 through 52
suits = ["hearts", "diamonds", "clubs", "spades"]
numbers = range(2, 11)
faces = ["jack", "queen", "king", "ace"]
cards = []
deck_of_cards = {}

for suit in suits:
	for number in numbers:
		cards.append(str(number) + " of " + suit)
	for face in faces:
		cards.append(face + " of " + suit)
for i in range(1, 53):
	deck_of_cards[i] = cards[i-1]

#Shuffle all cards
shuffled_deck = random.sample(range(1, 53), 52)

#Pairs collected by user
user_pairs = []

#to do if computer plays too
#Pairs collected by computer
#computer_pairs_num = 0
#computer_pairs = []


#pulls a card and removes from shuffled deck
def card_draw(x):
	shuffled_deck.pop(0)
	x -= 1
	if x >= 1:
            card_draw(x)


#displays "cards"
def display_hand(x):
	hand = []
	for i in x:
	    hand.append(deck_of_cards[i])
	#print hand
	return hand


#ask for a card
def ask_for_card(c):
    keys = range(1, 14)
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
    words = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
    for i, j, k in zip(keys, cards, words):
	if c == j or c == k:
            c = i
            #print c
            checking_computer_hand(c)
       

# checking computer hand for queried card
def checking_computer_hand(x):
    for i in computer_hand:
        if i % 13 == x % 13:
            computer_hand.remove(i)
            player_hand.append(i)
            look_for_pairs(player_hand)
            break
    else:
        print "\n","                GO FISH!!!!!!!!!", "\n"
        player_hand.append(shuffled_deck[0])
        card_draw(1)


#looking for pairs in hand
def look_for_pairs(hand):
    for i in hand:
        for j in hand:
            if i != j:
                if i % 13 == j % 13:
		    user_pairs.append(i)
                    user_pairs.append(j)
                    player_hand.remove(i)
                    player_hand.remove(j)
		   

####Deal First Hand

#computer hand
computer_hand = shuffled_deck[0:7]
#print "the computer hand:", computer_hand
card_draw(7)
#display_hand(computer_hand)


#player hand
player_hand = shuffled_deck[0:7]
card_draw(7)
#look_for_pairs(player_hand)
#print "Your hand = ", display_hand(player_hand)
#print "the player hand:", player_hand




######Main Game Play
print "\n", "\n"
print "==================================================================="
print " Welcome to kind of \"go fish\" ..you will win if you are patient."
print "                (For people who hate to lose)"
print " Ask the computer for its cards....and it gives them to you!!!"
print "                 Ask by number or face value"
print "===================================================================", "\n"
while True:
    if not computer_hand:
        print "                You win !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        exit()
    else:
	print "\n", "The computer has", len(computer_hand),"cards","\n"
        print "Your hand =====> ", display_hand(player_hand), "\n"
        #print "Computer =====> ", display_hand(computer_hand)
        look_for_pairs(player_hand)
        card_query = raw_input("Which card would you like to ask for?  ")
    	ask_for_card(card_query)
	print "Your pairs ====>>> " , display_hand(user_pairs), "<======","\n"
    

