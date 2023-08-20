import random
import common

word_list = ["mouse", "snake", "tiger"]
chosen_word = random.choice(word_list)

print(f"Psst! The chosen word is {chosen_word}")

display = []
word_length = len(chosen_word)
end_of_game = False
containGuess = False

#TODO - 1- Create a variable called lives to keep track of the number of lives left
lives = len(common.stages)

for char in chosen_word:
    display.append("_")

while(not end_of_game):
    containGuess = False
    guess = input("Guess a letter \n").lower()

    for iter in range(0, word_length):
        if(guess == chosen_word[iter]):
            display[iter] = guess
            containGuess = True

    #TODO - 2 - If guess is not a letter in the chosen word, reduce lives by 1. If lives goes down to 0, the game stops and you lose
    if(not containGuess):
        lives -= 1
        if(lives == 0):
            end_of_game = True
            print("You lose")

    print(display)

    if("_" not in display):
        end_of_game = True
        print("You win!")

    #TODO - 3 - Print the ASCII art from stages that corresponds to the current number of lives user has remaining
    print(common.stages[lives])