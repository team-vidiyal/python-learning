# Rock, Paper ->  computer (paper) winner
# Paper, Rock -> You win (paper)
# Scissor, rock -> rock winner

# scissor, paper -> scissor
import random


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

options = [ rock, paper, scissors ]

user_input = int(input("Enter 0 for rock, 1 for paper or 2 for scissors: "))

your_choice = options[user_input ]


print(f"Your choice: {your_choice}")

computer_generated_number = random.randint(0, 2)

print(f"computer_chosen_number : {computer_generated_number}")

computer_choice = options[computer_generated_number]

print(f"Computer's choice: {computer_choice}")

# you chose rock -> rock tie
             #    -> paper computer win
             #    > scissor you win
if user_input  == 0 and computer_generated_number == 0:
    print("It is a tie")
elif user_input  ==0 and computer_generated_number ==1:
    print("computer win")

elif user_input  ==0 and computer_generated_number ==2:
    print("you win")

elif user_input  ==1 and computer_generated_number ==0:
    print("you win")
elif user_input  ==1 and computer_generated_number ==1:
    print("Its a tie")
elif user_input  ==1 and computer_generated_number ==2:
    print("computer win")

elif user_input  ==2 and computer_generated_number ==0:
    print("Computer win")
elif user_input  ==2 and computer_generated_number ==1:
    print("you win")
elif user_input  ==2 and computer_generated_number ==2:
    print("Its a tie")



