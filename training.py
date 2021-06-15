import random

#Function to get the user input for choice of low roller or high roller (cash amount)
def getStatus(choices):
  status = ""
  while status not in choices:
      print("Low Roller = $50")
      print("High Roller = $100")
      status = input("Pick your status in the casino [%s]: " % ", ".join(choices))
  return status

#Function to get user input for which game to be played
def getGame(choices):
    game = ""
    while game not in choices:
        game = input("Which game would you like to play [%s]: " % ", ".join(choices))
    return game

#Prompt the user for how much $ to have for casino game
status = getStatus(["Low Roller", "High Roller"])
if status == "Low Roller":
    bankroll = 50
else:
    bankroll = 100

#Prompt user to choose which game to play
game = getGame(["Blackjack", "Craps", "Roulette"])

if game == "Blackjack":

