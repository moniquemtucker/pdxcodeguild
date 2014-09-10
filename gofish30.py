import random

counter = 1

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
player_pairs = []

#to do if computer plays too
#Pairs collected by computer
#computer_pairs_num = 0
computer_pairs = []


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


#ask for a card from player
def ask_for_card(c):
    keys = range(1, 14)
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
    words = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
    for i, j, k in zip(keys, cards, words):
	if c == j or c == k:
            c = i
            #print c
            checking_hand(c, computer_hand, player_hand, player_pairs)
 

#computer asks for card
def computer_query(hand):
    i = random.choice(hand)
    print "The computer is asking for a", deck_of_cards[i]
    checking_hand(i, player_hand, computer_hand, computer_pairs)



# checking a hand for queried card
def checking_hand(card, hand, other_hand, other_pairs):
    """
    param card: card queried by player 1
    param hand: player 2 hand
    param other_hand: player 1 hand
    param: other_pairs:player 1 pairs
    """
    for i in hand:
        if i % 13 == card % 13:
            hand.remove(i)
            other_hand.append(i)
            look_for_pairs(other_hand, other_pairs)
            break
    else:
        print "\n","                GO FISH!!!!!!!!!", "\n"
        other_hand.append(shuffled_deck[0])
        card_draw(1)





def look_for_pairs(hand,pairs):
    for i in hand:
	for j in hand:
	    if i != j:
	        if i % 13 == j % 13:
		    pairs.append(i)
	            pairs.append(j)
	            hand.remove(i)
	            hand.remove(j)


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


print "\n", "\n"
print "==================================================================="
print "                      Welcome to Go Fish!"
print " Ask the computer for its cards to try and make a pair!"
print "                 The one with the most pairs wins!"
print "                    (ask by number or face value)"
print "===================================================================", "\n"

while True:
    if not shuffled_deck and (not computer_hand or not player_hand):
        if len(computer_pairs) > len(player_pairs):
            print "computer wins!" 
	    exit()
        else:
            print "You win"
            exit()




    else:
        
        if counter %2 == 0:
            if not computer_hand:
                computer_hand = shuffled_deck[0:7]
	    else:
                computer_query(computer_hand)
                counter += 1
        
        else:
            if not player_hand:
                print"You get to draw more cards"
                player_hand = shuffled_deck[0:7]
            else:        
	        print "\n", "The computer has", len(computer_hand),"cards and", len(computer_pairs)/2,"pairs.","\n"
                print "Your hand =====> ", display_hand(player_hand), "\n"
                #print "Computer =====> ", display_hand(computer_hand)
                look_for_pairs(player_hand, player_pairs)
                card_query = raw_input("Which card would you like to ask for?  ")
                ask_for_card(card_query)
	        print "Your pairs ====>>> ", len(player_pairs)/2, "<======","\n"
                counter += 1













#def transfering_cards(hand, other_hand)


#card is the queried card
#hand is what the card is checking against
#other hand is the one asking
#other pairs is the askers pairs

#checking_hand(card, hand, other_hand, other_pairs)

