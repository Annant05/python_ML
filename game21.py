# game of 21
from random import choice


def select_card():
    acard = int(input("Enter a Card "))
    if acard not in cards:
        print("Please Reselect Card")
        return select_card()
    else:
        return acard


cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
playerScore = 0
cpuScore = 0
while not (playerScore >= 21 or cpuScore >= 21):
    print("Player TURN Available Cards :  " + str(cards))
    card = select_card()
    playerScore = playerScore + card
    cards.remove(card)

    selectedCard = choice(cards)  # randomCard()
    cpuScore = cpuScore + selectedCard
    cards.remove(selectedCard)
    print("\nPlayer Score : " + str(playerScore) + "\tCPU Score : " + str(cpuScore))

if playerScore >= 21:
    print("\n Player Win \nScore : " + str(playerScore))
elif cpuScore >= 21:
    print("\n CPU Win \nScore : " + str(cpuScore))
