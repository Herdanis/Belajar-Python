from replit import clear
import random

word_list = [
    "abandon",
    "saddle",
    "october",
    "machine",
    "language",
    "kangaroo",
    "gallery",
]

hangman = [
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
]

end_game = False
life = 6

chosen_word = random.choice(word_list)
display = []
for _ in range(len(chosen_word)):
    display += "_"

print(f"{' '.join(display)}")

while not end_game:
    guess = input("Guess a Letter: ").lower()
    clear()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        life -= 1
        print(f"{hangman[life]}")
        print(f"Wrong letter you have {life} chance")
        if life == 0:
            print("You lose!")
            end_game = True

    if "_" not in display:
        end_game = True
