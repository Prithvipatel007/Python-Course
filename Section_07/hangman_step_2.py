import random

word_list = ["mouse", "snake", "tiger"]
chosen_word = random.choice(word_list)

print(f"Psst! The chosen word is {chosen_word}")

#TODO -1 - Create an empty list called display. For each letter in the chosen word, add a "_" to display
display = []
word_length = len(chosen_word)

for char in chosen_word:
    display.append("_")

guess = input("Guess a letter \n").lower()

#TODO -2 - Loop through each position in the chosen word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position

for iter in range(0, word_length):
    if(guess == chosen_word[iter]):
        display[iter] = guess


#TODO -3 - Print 'display' and you should see the guessed letter in the correct position and every other letter repace with _
print(display)