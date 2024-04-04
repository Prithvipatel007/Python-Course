import random
import common

chosen_word = random.choice(common.word_list)

print(common.logo)

# Create Blanks
display = []
word_length = len(chosen_word)
end_of_game = False
containGuess = False

lives = len(common.stages)

for char in chosen_word:
    display.append("_")

while(not end_of_game):
    containGuess = False
    guess = input("Guess a letter \n").lower()

    #TODO - 3 - If the user has entered a letter they have guessed, print the letter and let them know
    if guess in display:
        print(f"You have already guessed {guess}")

    for iter in range(0, word_length):
        if(guess == chosen_word[iter]):
            display[iter] = guess
            containGuess = True

    if(not containGuess):
        #TODO - 4 - If the letter is not in the chosen word, print out the letter and let them know it's not in the word
        print(f"You guessed letter {guess}, that's not in the word. you lose a life")
        lives -= 1
        if(lives == 0):
            end_of_game = True
            print("You lose")
            print(f"The correct word was {chosen_word}")

    print(display)

    if("_" not in display):
        end_of_game = True
        print("You win!")

    print(common.stages[lives])