"""
You are playing a game with one of your villagers. In the game, 
there are two players where their respective scores are incremented 
by one point at a time. Given an array of booleans, where True means 
that Player 1 scores a point, and False means that Player 2 scores a 
point. Write a program that outputs the winner of the game. If there 
is no winner, return 0.
"""


def getWinner(gameScores):
    counter = 0
    for i in range(len(gameScores)):
        if gameScores[i] is True:
            counter += 1
    if counter == len(gameScores) // 2 and len(gameScores) % 2 == 0:
        return 0
    elif counter > len(gameScores) // 2:
        return 1
    else:
        return 2


def main():
    print(getWinner([True, False, True, False, False, False]))
    print(getWinner([True, False, True, False, True, False, True]))
    print(getWinner([True, False]))
    print("The values above should be 2, 1, and 0.")
