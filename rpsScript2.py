# ROCK PAPER SCISSORS (IMPROVED)
# Author: Nahdaa Jawed
# Date Started: 31/03/2023 17:06
# Date Finished: 31/03/2023 17:50
# Description:  A best-of-three game of rock, paper, scissors against the computer!
#               The user is prompted to choose rock, paper or scissors, and the computer randomly chooses as well.
#               The results are then compared and printed, and the game number and winner is recorded.
#               At the end of the three games, the final winner is printed to the screen.

# Importing relevant modules and functions.
import random

# Defining the game as a function
def rockPaperScissors():
    # Initialising variables.
    bestOfThree = 0
    compWin = 0
    userWin = 0
    gameNumber = bestOfThree+1

    print("\nLet's play best of three!")
    while bestOfThree!=3:
        userChoice = input(f"\nGame {gameNumber}: Do you choose rock, (r), paper (p) or scissors (s)? ").lower()
        compChoice = random.choice(["r", "p", "s"])

        if userChoice == compChoice:
            print(f"The computer also chose {compChoice}, its a draw!")
            bestOfThree = bestOfThree + 1
            gameNumber = gameNumber +1

        elif winGame(userChoice, compChoice):
            print(f"The computer chose {compChoice}, you win!")
            bestOfThree = bestOfThree + 1
            userWin = userWin + 1
            gameNumber = gameNumber + 1

        else:
            print(f"The computer chose {compChoice}, you lose!")
            bestOfThree = bestOfThree + 1
            compWin = compWin + 1

    # Displaying results for the best-of-three.
    if compWin > userWin:
        print("\nResults:\nThe computer won 2 out of 3 games. The computer wins overall!")

    elif userWin > compWin:
        print("\nResults:\nYou won 2 out of 3 games. You won overall!")

    else:
        print("\nResults:\nYou and the computer drew one or three games. Its a draw overall!")

# Defining a function for if the user wins.
def winGame(user, computer):
    if (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
        return True

rockPaperScissors()
