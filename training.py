import random

#Function to get the user input for choice of low roller or high roller (cash amount)
def getStatus(choices):
  status = ""
  while status not in choices:
      print("Low Roller = $50")
      print("High Roller = $100")
      status = input("Welcome to the Casino! Choose your status for the night [%s]: " % ", ".join(choices))
  return status

#Function to get mode
def getMode(choices):
    mode = ""
    while mode not in choices:
        mode = input("Would you like the instructions printed? [%s]: " % ", ".join(choices))
    return mode

#Function to get user input for which game to be played
def getGame(choices):
    game = ""
    while game not in choices:
        game = input("Which game would you like to play [%s]: " % ", ".join(choices))
    return game

#Function to get users choice on whether to hit or stand
def getChoice(choices):
    choice = ""
    while choice not in choices:
        choice = input("Choose whether to hit or stand: [%s]: " % ", ".join(choices))
    return choice


import random


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # Implementing build in methods so that you can print a card object
    def __unicode__(self):
        return self.show()

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return "{} of {}".format(val, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
        self.values = []

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print(card.show())

    # Generate 52 cards
    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    # Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length - 1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
            # You can also use the build in shuffle method
            # random.shuffle(self.cards)

    # Return the top card
    def deal(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    # Display all the cards in the players hand
    def showHand(self):
        if len(self.hand) < 2:
            self.hand.append("Flipped Card")
        else:
            if "Flipped Card" in self.hand: self.hand.remove("Flipped Card")
        print("{} hand: {}".format(self.name, self.hand))
        return self

    def handVals(self):
        return self.hand

#Prompt the user for how much $ to have for casino game
status = getStatus(["Low Roller", "High Roller"])
if status == "Low Roller":
    bankroll = 100
else:
    bankroll = 250

print("To beat the Casino you have to reach $500 if you reach $0 the Casino beats you")

#Prompt user to choose which game to play
game = getGame(["Blackjack", "Craps", "Roulette"])
mode = getMode(["Yes", "No"])
#while bankroll != 0 or bankroll != 500:
if game == "Blackjack":
    if mode == 'Yes':
        print('''\nBasic rules of Blackjack:
            •The goal of blackjack is to beat the dealer's hand without going over 21.,
            •Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.
            •Each player starts with two cards, one of the dealer's cards is hidden until the end.
            •To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
            •If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
            •If you are dealt 21 from the start (Ace & 10), you got a blackjack.
            •Dealer will hit until his/her cards total 17 or higher.
            •Doubling is like a hit, only the bet is doubled and you only get one more card.
            •Split can be done when you have two of the same card - the pair is split into two hands.
                ''')
    else:
        pass

    deck = Deck()
    deck.shuffle()
    #deck.show()

    #Prints player hand
    print('\nDealing cards...')
    myDeck = Deck()
    myDeck.shuffle()
    player = Player('Your')
    player.draw(myDeck, 2)
    player.showHand()
    x = player.handVals()
    # print(x[0].value)
    # print(x[1].value)

    #Prints dealers hand
    dealer = Player("Dealer's")
    dealer.draw(myDeck, 1)
    print("\n")
    dealer.showHand()
    dealer.draw(myDeck, 1)
    dealer.showHand()
    x = dealer.handVals()
    # print(x[0].value)

    #Hit or stand
    choice = getChoice(["Hit", "Stand"])
    if choice == stand:
        pass


