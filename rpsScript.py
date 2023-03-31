# ROCK PAPER SCISSORS
# Author: Nahdaa Jawed
# Date Started: 31/03/2023 16:30
# Date Finished: 31/03/2023 16:55
# Description:  A simple rock, paper, scissors game where the user and computer both choose either r, p, or s.
#               The results of who won is then printed.


#Importing relevant modules and functions.
import random

# Defining the game as a function.
def rockPaperScissors():
    userChoice = input("Do you choose rock (r), paper (p) or scissors (s)? ").lower()
    programChoice = random.choice(["r","p","s"])

    # If the user chooses rock.
    if userChoice == "r":
        if programChoice == "r":
            print ("The computer chose rock too! It's a draw!")

        elif programChoice == "p":
            print("The computer chose paper, you lose!")

        elif programChoice == "s":
            print("The computer chose scissors, you win!")

    # If the user chooses paper.
    elif userChoice == "p":
        if programChoice == "p":
            print("The computer chose paper too! It's a draw!")

        elif programChoice == "s":
            print("The computer chose scissors, you lose!")

        elif programChoice == "r":
            print("The computer chose rock, you win!")

    # If the user chooses scissors.
    elif userChoice == "s":
        if programChoice == "s":
            print("The computer chose scissors too! It's a draw!")

        elif programChoice == "r":
            print("The computer chose rock, you lose!")

        elif programChoice == "p":
            print("The computer chose paper, you win!")


rockPaperScissors()