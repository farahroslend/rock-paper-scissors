import random

# ASCII Arts for rock, paper, and scissors by Veronica Karlsson

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

options=[rock, paper, scissors]

user_throw=int(input("Make your choice either rock, paper or scissors (0, 1, or 2):"))

computer_throw=random.randint(0,2)


if user_throw==computer_throw:
  print(options[user_throw])
  print("Computer:/n")
  print(options[computer_throw])
  print("IT'S A TIE.")
elif str(user_throw)+str(computer_throw) == '01' or str(user_throw)+str(computer_throw) == '12' or str(user_throw)+str(computer_throw) == '20':
  print(options[user_throw])
  print("Computer:\n")
  print(options[computer_throw])
  print("SORRY! YOU LOSE...")

else:
  print(options[user_throw])
  print("Computer:/n")
  print(options[computer_throw])
  print("CONGRATULATIONS! YOU WIN!")
