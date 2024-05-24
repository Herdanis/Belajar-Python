import random

option = ["r", "p", "s"]
user_point = 0
computer_point = 0


r = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

p = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

s = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

image = [r, p, s]

while True:
    print("Pick your poison (R)ock / (P)aper / (S)cissor :")
    user_input = input("(Q) to End the game ").lower()
    if user_input == "q":
        break
    elif user_input not in option:
        print("Invalid Input!")
        continue
    random_number = random.randint(0, 2)
    computer_pick = option[random_number]
    index_image = option.index(user_input)
    print("User Picked")
    print(image[index_image])

    print("Computer Picked")
    print(image[random_number])

    if user_input == "r" and computer_pick == "s":
        print("You Won!")
        user_point += 1
    elif user_input == "p" and computer_pick == "r":
        print("You Won!")
        user_point += 1
    elif user_input == "s" and computer_pick == "p":
        print("You Won!")
        user_point += 1
    elif user_input == computer_pick:
        print("Draw!")
    else:
        print("You Lose!")
        computer_point += 1

print(f"You won, {user_point} times.")
print(f"Computer won, {computer_point} times.")
quit("Goodbye!")
