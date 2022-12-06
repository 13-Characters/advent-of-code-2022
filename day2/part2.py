import numpy as np
input = open("input.txt")

opponent = ['A', 'B', 'C']
you = ['X', 'Y', 'Z']
totalPoints = 0
for round in input:
    winningMove = (opponent.index(round[0]) + 1) % 3
    losingMove = (opponent.index(round[0]) - 1) % 3
    tieMove = opponent.index(round[0])

    ## Need to win condition
    if round[2] == 'Z':
        totalPoints = totalPoints + 6 + (winningMove + 1)
    ## Need to tie condition
    if round[2] == 'Y':
        totalPoints = totalPoints + 3 + (tieMove + 1)
    ## Need to lose condition
    if round[2] == 'X':
        totalPoints = totalPoints + (losingMove + 1)

print(totalPoints)