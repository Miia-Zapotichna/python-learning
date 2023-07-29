import random

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)

guess = input("Guess the letter:").lower()

display = []
for letter in chosen_word:
    display += "_"

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)
