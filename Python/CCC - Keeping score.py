# Keeping Score #
# October 21, 2018
# By Robin Nash

class Suit:
    def __init__(self,suit,suitName):
        self.suit = suit
        self.name = suitName
        self.kings = suit.count("K")
        self.queens = suit.count("Q")
        self.jacks = suit.count("J")
        self.aces = suit.count("A")

        self.void = len(suit)==0
        self.singleton = len(suit)==1
        self.doubleton = len(suit)==2

    def points(self):
        points = 0
        points+=self.aces*4
        points+=self.kings*3
        points+=self.queens*2
        points+=self.jacks
        if self.void:
            points+=3
        if self.singleton:
            points+=2
        if self.doubleton:
            points+=1
        return(points)

hand = input()
clubs = Suit(hand[hand.find("C")+1:hand.find("D")],"Clubs")
diamonds = Suit(hand[hand.find("D")+1:hand.find("H")],"Diamonds")
hearts = Suit(hand[hand.find("H")+1:hand.find("S")],"Hearts")
spades = Suit(hand[hand.find("S")+1:],"Spades")

suits = [clubs,diamonds,hearts,spades]
print("Cards Dealt              Points")
total = 0
for suit in suits:
    total += suit.points()
    print(suit.name,end=" ")
    for card in suit.suit:
        print(card, end=" ")
    print(" "*(29-len(suit.name)-len(suit.suit)*2-len(str(suit.points()))),suit.points())
print("                       Total",total)


    
#1540160866.0