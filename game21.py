# game of 21
from random import choice


def checkCardorReselect():
    card = int(input("Enter a Card "))
    if (card not in cards):
        print("Please Reselect Card")
        return checkCardorReselect()
    else:
        return card


cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
playerScore = 0
cpuScore = 0
while (not (playerScore >= 21 or cpuScore >= 21)):
    print("Player TURN Avaliable Cards :  " + str(cards))
    card = checkCardorReselect()
    playerScore = playerScore + card
    cards.remove(card)
    print("Player Score : " + str(playerScore))

    selectedCard = choice(cards)  # randomCard()
    cpuScore = cpuScore + selectedCard
    cards.remove(selectedCard)
    print("CPU Score : " + str(cpuScore))

if (playerScore >= 21):
    print("\n Player Win \nScore : " + str(playerScore))
elif (cpuScore >= 21):
    print("\n CPU Win \nScore : " + str(cpuScore))
