import string
import random

letters = list(string.ascii_letters)
numbers = [str(i) for i in range(10)]
special_char = ["*", "!", "+", "|", "-", "&"]

print("Password Generator!")

password_list = []

for char in range(0, random.randint(6, 9)):
    password_list.append(random.choice(letters))

for char in range(0, random.randint(3, 7)):
    password_list.append(random.choice(numbers))

for char in range(0, random.randint(1, 2)):
    password_list.append(random.choice(special_char))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Here Your the Password: {password}")
