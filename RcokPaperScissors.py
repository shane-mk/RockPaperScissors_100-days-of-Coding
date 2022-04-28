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

#Write your code below this line 👇
import random
comp_choice = random.randint(0, 2)
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Scissors, 2 for Paper "))
if user_choice == 0:
    print(rock)
elif user_choice == 2:
    print(paper)
elif user_choice == 1:
    print(scissors)
else:
    print("invalid input")
print(f"the computer chose: ")
if comp_choice == 0:
    print(rock)
elif comp_choice == 2:
    print(paper)
elif comp_choice == 1:
    print(scissors)
else:
    print("invalid input")
if user_choice == comp_choice:
    print("Tie")
else:
    if user_choice == 0 and comp_choice == 1:
        print("You win")
    elif user_choice == 0 and comp_choice == 2:
        print("You lose")
    elif user_choice == 1 and comp_choice == 2:
        print("You win")
    elif user_choice == 1 and comp_choice == 0:
        print("You lose")
    elif user_choice == 2 and comp_choice == 0:
        print("You win")
    elif user_choice == 2 and comp_choice == 1:
        print("You lose")
    else:
        print("something went wrong")
print("thanks for playing")
