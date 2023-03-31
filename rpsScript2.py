# ROCK PAPER SCISSORS (IMPROVED)
# Author: Nahdaa Jawed
# Date Started: 31/03/2023 17:06
# Date Finished: -
# Description:

import random

def rockPaperScissors():
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

        elif winGame(userChoice, compChoice):
            print(f"The computer chose {compChoice}, you win!")
            bestOfThree = bestOfThree + 1
            userWin = userWin + 1

        else:
            print(f"The computer chose {compChoice}, you lose!")
            bestOfThree = bestOfThree + 1
            compWin = compWin + 1

    if compWin > userWin:
        print("\nResults:\nThe computer won 2 out of 3 games. The computer wins overall!")

    elif userWin > compWin:
        print("\nResults:\nYou won 2 out of 3 games. You won overall!")

    else:
        print("\nResults:\nYou and the computer drew one or three games. Its a draw overall!")

def winGame(user, computer):
    if (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
        return True

rockPaperScissors()
