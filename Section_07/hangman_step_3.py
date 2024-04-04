import random

word_list = ["mouse", "snake", "tiger"]
chosen_word = random.choice(word_list)

print(f"Psst! The chosen word is {chosen_word}")

display = []
word_length = len(chosen_word)
end_of_game = False

for char in chosen_word:
    display.append("_")



#TODO - 1 - Use a while loop to let user guess again. The loop should only stop when there is no "_" in display

while(not end_of_game):
    guess = input("Guess a letter \n").lower()

    for iter in range(0, word_length):
        if(guess == chosen_word[iter]):
            display[iter] = guess

    print(display)

    if("_" not in display):
        end_of_game = True
        print("You win!")