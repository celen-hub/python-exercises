rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = input("Rock, Paper, Scissors choose wisely! :")
import random
x = random.randint(1,3)

if choice == "Rock":
  print(rock)
elif choice == "Paper":
  print(paper)
else:
  print(scissors)

if x == 1:
  print("Comp's choice :\n ")
  print(rock)
elif x == 2:
  print("Comp's choice :\n")
  print(paper)
else:
  print("Comp's choice :\n")
  print(scissors)
  
if choice == "Rock" and x == 1:
  print("Even do it agane")
elif choice == "Rock" and x == 2:
  print("Comp got you EZ")
elif choice == "Rock" and x == 3:
  print("You do rock indeed!")
elif choice == "Paper" and x == 1:
  print("LUL you so cool got that bastardo")
elif choice == "Paper" and x == 2:
  print("Same shit ")
elif choice == "Paper" and x == 3:
  print("you so noob xd")
elif choice == "Scissors" and x == 1:
  print("Here i am rock you like you loser!")
elif choice == "Scissors" and x == 2:
  print("Good slice nice one!")
elif choice == "Scissors" and x == 3:
  print("Same shit go agane")