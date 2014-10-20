__author__ = 'Monique Tucker'

ones = (1, 3, 5, 7)

hand = [1, 14, 24]

def look_for_pairs(hand):
    pair_set = []
    for a in hand:
        if a in ones:
            pair_set.append(a)
    return(pair_set)

look_for_pairs(hand)


#test that 'look for pairs' function accurately finds a match between 'ones' list and hand then appends to pair set list
def test_answer():
    assert look_for_pairs([2, 3]) == [3]