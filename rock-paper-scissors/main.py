import random 
# ROCK
rock = """
	ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
# PAPER
paper = """
	PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
# SCISSORS 
scissors = """
	SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices_list = [rock,paper,scissors]
random_generator = random.randint(0,2)
random_choice = choices_list[random_generator]

user_choice_num = int(input("Enter 1 for rock, 2 for paper, 3 scissors: ")) -1
user_choice = choices_list[user_choice_num]

print(f" YOU CHOSE:\n{user_choice}")
print(f"COMPUTER CHOSE:\n{random_choice}")

print(random_generator)
print(user_choice_num)
# Conditions 

# Draw Condition
if random_generator == user_choice_num:
	print("Its a Draw")
elif random_generator == 0 and user_choice_num == 2:
	print("Computer Wins")
elif random_generator == 1 and user_choice_num == 0:
	print('Computer Wins')
elif random_generator == 2 and user_choice_num == 1:
	print("Computer Wins")
else:
	print("invalid error occured ")
