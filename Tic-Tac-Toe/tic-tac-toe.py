"""
    Created by Devansh on 11-08-2020
"""
import random
from time import sleep


def displayBoard():
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("-+-+-")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("-+-+-")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])


def isWinning(player):
    if board[0][0] == board[0][1] == board[0][2] == player or \
            board[1][0] == board[1][1] == board[1][2] == player or \
            board[2][0] == board[2][1] == board[2][2] == player or \
            board[0][0] == board[1][1] == board[2][2] == player or \
            board[0][2] == board[1][1] == board[2][0] == player or \
            board[0][0] == board[1][0] == board[2][0] == player or \
            board[0][1] == board[1][1] == board[2][1] == player or \
            board[0][2] == board[1][2] == board[2][2] == player:
        return True


def chance(player):
    x, y = map(int, input().strip().split())
    while x < 0 or y < 0 or x > 3 or y > 3 or board[x - 1][y - 1] != " ":
        print("Wrong input! Try again")
        x, y = map(int, input().strip().split())
        if board[x - 1][y - 1] != " ":
            print("The place is already occupied, enter another values:")
            x, y = map(int, input().strip().split())
    board[x - 1][y - 1] = player


def computer(player):
    moves = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    x, y = moves[random.randrange(0, 8)]
    if board[x - 1][y - 1] != " ":
        x, y = moves[random.randrange(0, 8)]
    board[x - 1][y - 1] = player
    sleep(1)
    displayBoard()


print("Who do you want to play against?")
print("Enter 1 to play against Computer")
print("Enter 2 to play against your player i.e a 2 player game")
play = int(input("Enter your choice:")) - 1

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player1 = input("Player 1, what do you choose?(X/O) :")
while player1 != "X" and player1 != "O":
    print("Wrong input! Please try again")
    player1 = input("What do you choose?(X/O) :")

player2 = ("O", "X")[player1 == "O"]
displayBoard()

entry = 9

running = True

while running:
    print("It's player 1's turn, enter the row and column number, separated by spaces, where you want to put your "
          "piece:")
    chance(player1)
    displayBoard()
    entry -= 1
    if isWinning(player1):
        print("Player 1 won!!!")
        break
    if entry == 0:
        print("DRAW!!!")
        break

    if play == 0:
        print("It is computer's turn.")
        computer(player2)
        entry -= 1
        if isWinning(player2):
            print("Computer won!!!")
            break

    elif play == 1:
        print("It's player 2's turn, enter the row and column number, separated by spaces, where you want to put your "
              "piece:")
        chance(player2)
        displayBoard()
        entry -= 1
        if isWinning(player2):
            print("Player 2 won!!!")
            break

print("Thank you for playing.")
