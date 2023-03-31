# ROCK PAPER SCISSORS (IMPROVED)
# Author: Nahdaa Jawed
# Date Started: 31/03/2023 17:06
# Date Finished: -
# Description:

import random

def rockPaperScissors():
    userChoice = input("Do you choose rock, (r), paper (p) or scissors (s)? ").lower()
    compChoice = random.choice(["r","p","s"])

    if userChoice == compChoice:
        print(f"The computer also chose {compChoice}, its a draw!")

    elif winGame(userChoice, compChoice):
        print(f"The computer chose {compChoice}, you win!")

    else:
        print(f"The computer chose {compChoice}, you lose!")

def winGame(user, computer):
    if (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
        return True

rockPaperScissors()
