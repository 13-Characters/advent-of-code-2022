import numpy as np
input = open("input.txt")

opponent = ['A', 'B', 'C']
you = ['X', 'Y', 'Z']
totalPoints = 0
for round in input:
    winningMove = (opponent.index(round[0]) + 1) % 3
    losingMove = (opponent.index(round[0]) - 1) % 3
    tieMove = opponent.index(round[0])

    totalPoints = totalPoints + you.index(round[2]) + 1
    ## Winning condition
    if round[2] == you[winningMove]:
        totalPoints = totalPoints + 6
    ## Tie condition
    if round[2] == you[tieMove]:
        totalPoints = totalPoints + 3

print(totalPoints)