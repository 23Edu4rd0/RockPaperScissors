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

import random

player = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if player >= 3 or player < 0:
    print("You typed an invalid number. You lose!")
else:
    computer = random.randint(0, 2)

    choices = [rock, paper, scissors]

    print("\nYou chose:")
    print(choices[player])

    print("\nComputer chose:")
    print(choices[computer])

    if player == computer:
        print("Draw!")
    elif player == 0 and computer == 2 or player == 1 and computer == 0 or player == 2 and computer == 1:
        print("Player Win!")
    else:
        print("Computer Win!")
