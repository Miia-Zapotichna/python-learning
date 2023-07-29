import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


import hangman_words
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
end_of_game = False
lives = 6
display = []
for letter in chosen_word:
    display += "_"
while not end_of_game:

    guess = input("Guess the letter:").lower()

    contains = False

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            contains = True

    if contains == False:
        lives -= 1
        print(lives)

    print(display)
    if lives == 0:
        end_of_game = True
        print("You lost!")
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
