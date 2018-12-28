


# Solution to project Euler problem 54
# Problem:
"""In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

doc = open('poker_hands.txt')
doc = doc.read()
doc = doc.replace('\n','')
doc = doc.replace(' ','')
p1 = [doc[i:i+10] for i in range(0,19981,20)]
p2 = [doc[i:i+10] for i in range(10,19991,20)]

Ranks = {
    'high':0,
    '1pair':1,
    '2pair':2,
    '3ok':3,
    'strt':4,
    'flsh':5,
    'fh':6,
    '4ok':7,
    'sf':8,
    'rf':9
}
from itertools import cycle, islice
global values
values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
def winner(h1,h2):
    global values
    def straight(string):
        global values
        c = cycle(values)
        value = []
        for i in range(9):
            temp = ''
            for k in range(5):
                temp += next(c)
            for i in range(8):
                next(c)
            value.append(temp)
            next(c)
        if ''.join(sorted(string)[:5]) in value:
            return 4
        else:
            return threekind(string)

    def flush(string):
        if string.count('D')==5:
            return True
        if string.count('H')==5:
            return True
        if string.count('C')==5:
            return True
        if string.count('S')==5:
            return 5
        else:
            return straight(string)

    def sf(string):
        if flush(string) and straight(string):
            return 8
        return fourkind(string)

    def rf(string):
        if sf(string):
            if ''.join(sorted(string)[5:])=='AJKQT':
                return 9
        return sf(string)

    def threekind(player):
        for c in values:
            if player.count(c) == 3:
                return 3
        return twopairs(player)


    def fh(string):
        if threekind(string):
            s = string[::2]
            for i in values:
                if s.count(i) == 3:
                    s = s.replace(i,'')
                    break
            if s[0]==s[1]:
                return 6
        return flush(string)

    def fourkind(player):
        for c in values:
            if player.count(c) == 4:
                return 7
        return fh(player)

    def onepair(player):
        for c in values:
            if player.count(c) == 2:
                return 1
        return False

    def twopairs(player):
        count = 0
        for c in values:
            if player.count(c) == 2:
                count += 1
        if count == 2:
            return 2
        else:
            return onepair(player)

    global highcard
    def highcard(player):
        cards = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14,
        }
        temp = 0
        for i in player[::2]:
            if cards[i] > temp:
                temp = cards[i]
        return temp

    p1 = rf(h1) #one pair, return 1
    p2 = rf(h2) #nothing, false

    if p2 == p1:
        if p2 == 6:
            temp1 = 0
            temp2 = 0
            for i in values:
                if p2.count(i) == 3:
                    temp2 = int(i)
                if p1.count(i) == 3:
                    temp1 = int(i)
            if temp2>temp1:
                return 2
            elif temp1>temp2:
                return 1
        if highcard(h1) > highcard(h2):
            return 1
        if highcard(h2) > highcard(h1):
            return 2

    elif (p1 or p2) == False:
        if p1 == False:
            return 2
        else:
            return 1
    elif p1 > p2:
        return 1
    else:
        return 2

print(winner("5H5C6S7SKD", "2C3S8S8DTD"))

# count = 0
# for i in range(1000):
#     if winner(p1[i],p2[i])==1:
#         count += 1
# print(count)
