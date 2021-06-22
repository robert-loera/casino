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
        game = input("\nWhich game would you like to play [%s]: " % ", ".join(choices))
    return game

#Function to get users choice on whether to hit or stand
def getChoice(choices):
    choice = ""
    while choice not in choices:
        choice = input("Choose whether to hit or stand: [%s]: " % ", ".join(choices))
    return choice

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

def getBet(choices):
    size = ""
    while size not in choices:
        size = input("Choose your bet size [%s]: " % ", ".join(choices))
    size = size.strip("$")
    return int(size)

#Function to return the sum of all cards in hand as total
def getTotal(hand):
    valList = []
    total = 0
    for ele in range(0, len(hand)):
        if hand[ele].value > 10:
            valList.append(10)
        else:
            valList.append(hand[ele].value)
        total = sum(valList)
    return total

#Function that returns the sum of 2 dice being rolled
def diceSum():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("You rolled a " + str(die1) + " and a " + str(die2))
    total = die1 + die2
    return total


#Prompt the user for how much $ to have for casino game
status = getStatus(["Low Roller", "High Roller"])
if status == "Low Roller":
    bankroll = 100
else:
    bankroll = 250

print("To beat the Casino you have to reach $500 if you reach $0 the Casino beats you")
switch = "No"
#Prompt user to choose which game to play
game = getGame(["Blackjack", "Craps", "Roulette"])
mode = getMode(["Yes", "No"])
while bankroll > 0 and bankroll < 1000:
    if switch == "Yes":
        game = getGame(["Blackjack", "Craps", "Roulette"])
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
        print("\nCurrent bankroll amount $" + str(bankroll))
        betSize = getBet(["$5", "$20", "$50"])
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
        pHand = player.handVals()
        # print(pHand[0].value)
        # print(pHand[1].value)

        #Prints dealers hand
        dealer = Player("Dealer's")
        dealer.draw(myDeck, 1)
        print("\n")
        dealer.showHand()
        dealer.draw(myDeck, 1)
        #dealer.showHand()
        dHand = dealer.handVals()
        # print(dHand[0].value)

        playing = ""
        #Hit or stand
        while playing != "end":
            choice = getChoice(["Hit", "Stand"])
            pTotal = getTotal(pHand)
            if pTotal == 21:
                print("Blackjack! You won this hand")
                bankroll = bankroll + betSize
                playing = "end"

            elif choice == "Stand":
                print("\nYou chose to stand. Flipping dealer's face down card")
                dealer.showHand()
                dHand = dealer.handVals()
                dTotal = getTotal(dHand)
                while dTotal < 17:
                    print("\nDealer drawing another card")
                    dealer.draw(myDeck, 1)
                    dealer.showHand()
                    dTotal = getTotal(dHand)
                if dTotal > 21:
                    print("\nDealer busted, you win!")
                    bankroll = bankroll + betSize
                elif dTotal == 21:
                    print("\nDealer hit Blackjack, you lose")
                    bankroll = bankroll - betSize
                elif dTotal > pTotal:
                    print("\nDealer has higher hand, you lose")
                    bankroll = bankroll - betSize
                elif dTotal == pTotal:
                    print("\nPush")
                else:
                    print("You have the higher hand, you win!")
                    bankroll = bankroll + betSize
                playing = "end"

            elif choice == "Hit":
                print("\nDealing card")
                player.draw(myDeck, 1)
                player.showHand()
                pTotal = getTotal(pHand)
                if pTotal > 21:
                    print("You busted, dealer wins")
                    bankroll = bankroll - betSize
                    playing = "end"
                elif pTotal == 21:
                    print("Blackjack! You won this hand")
                    bankroll = bankroll + betSize
                    playing = "end"

        if bankroll > 0 and bankroll < 1000:
            switch = input("\nWould you like to switch games? Enter: Yes or No: ")

    if game == "Craps":
        if mode == 'Yes':
            print('''\nBasic rules of Craps:
                •  When you wager on the pass line, you are betting that either a 7 or an 11 will be the result of the 
                come-out roll. If a shooter rolls a 7 or 11 on the come-out roll, you double your money. If the shooter
                rolls a 4, 5, 6, 8, 9 or 10 instead, then a point is established. When you bet the Pass line, you want
                that point number to be rolled again, (before the shooter rolls a 7). If the shooter does hit the
                number before rolling a 7, your Pass line bet is doubled. If the shooter rolls a 2, 3 or 12 (or craps)
                on the come-out roll, then you lose your Pass line bet. If a point is established and a 7 is rolled 
                before that point value, this also results in a lost Pass line bet.
                    ''')
        print("\nCurrent bankroll amount $" + str(bankroll))
        betSize = getBet(["$5", "$20", "$50"])
        input("\nPress enter when you are ready to roll")
        print("\nFirst Roll")
        x = diceSum()
        if x == 7 or x == 11:
            print("You win!")
            bankroll = bankroll + betSize
        elif x == 2 or x == 3 or x == 12:
            print("Craps. You lose")
            bankroll = bankroll - betSize
        else:
            point = x
            print("\nYour point is " + str(x))
            while x != 7 and x != "point":
                input("\nPress enter when you are ready to roll")
                x = diceSum()
                if x == 7:
                    print("You sevened out. You Lose")
                    bankroll = bankroll - betSize
                if x == point:
                    print("You rolled your point. You Win")
                    bankroll = bankroll + betSize
                    x = "point"

        if bankroll > 0 and bankroll < 1000:
            switch = input("\nWould you like to switch games? Enter: Yes or No: ")


if bankroll <= 0:
    print("\nYou Lost")
else:
    print("\nCongrats you won!!!")