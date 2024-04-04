import random

word_list = ["mouse", "snake", "tiger"]

# TODO-1 - Randomly choose a word from the word list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)

# TODO-2 - Ask the use to guess a letter and assign their answer to a variable called guess. Make guess lowercase
guess = input("Guess a letter \n").lower()

# TODO-3 - Check if the letter the user guessed is one of the letters in the chosen_word
for letter in chosen_word:
    if(guess == letter):
        print("Right ")
    else:
        print("Wrong ")