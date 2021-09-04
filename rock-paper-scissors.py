"""
COMPUTER RANDOMLY CHOOSES BETWEEN ROCK, PAPER AND SCISSORS
USER GIVES INPUT OUT OF ROCK PAPER AND SCISSORS 
PRINTS IMAGE 
"""
import random
items = ["rock","scissors","paper"]

player = input("rock paper or scissors")


computer = random.choice(items)

if player == computer:
    print(computer)
    print("draw")
if player == "rock" and computer == "paper":
    print(""" YOU PLAYED
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    print(""" COMPUTER PLAYED
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    print("computer wins")
if player == "paper" and computer == "scissors":
    print(""" YOU PLAYED
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    print(""" COMPUTER PLAYED
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    print("computer wins")
if player == "scissors" and computer == "rock":
    print(""" YOU PLAYED
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    print(""" COMPUTER PLAYED
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    print("COMPUTER WINS")
if player == "paper" and computer == "rock":
    print(""" YOU PLAYED
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    print(""" COMPUTER PLAYED
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    print("PLAYER WINS")
if player == "scissors" and computer == "paper":
    print(""" YOU PLAYED
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    print(""" COMPUTER PLAYED
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    print("player wins")
if player == "rock" and computer == "scissors":
    print(""" YOU PLAYED
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    print(""" COMPUTER PLAYED
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    print("player wins")
