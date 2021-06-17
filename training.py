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

#Class to handle all card functions
class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

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
    player = Player("Player1")
    print("\nYour Hand")
    player.draw(deck).draw(deck)
    player.showHand()

    #Prints dealers hand
    dealer = Player("Dealer")
    print("\nDealer Hand")
    dealer.draw(deck)
    dealer.showHand()
    print("Flipped card")
    dealer.draw(deck)

