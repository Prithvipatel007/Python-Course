from common import logo
import random
import os

easy_list = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def play_game():

  print(logo)
  print(" Think of a number between 1 and 100")

  is_game_over = False
  userChoice = 0

  difficulty = input("Choose the difficulty: Type 'easy' or 'hard' ").lower()

  if(difficulty == "easy"):
    computerChoice = random.choice(easy_list)
    attempts = EASY_ATTEMPTS
  elif(difficulty == "hard"):
    computerChoice = random.randint(1,100)
    attempts = HARD_ATTEMPTS
  else:
    is_game_over = True

  while(is_game_over != True):
    userChoice = int(input("Enter your guess : "))
    print(f"You have chosen {userChoice}")

    if( userChoice == computerChoice):
        print(f"Your guess is correct! The number is {computerChoice}")
        is_game_over = True
    else:
        if(userChoice > computerChoice):
            print("The number is a bit lower than your guess")
        elif(userChoice < computerChoice):
            print("The number is a bit higher than your guess")

        attempts -= 1
        print(f"You have guessed it wrong! Try again! You have {attempts} attempts left")
        
    if(attempts == 0):
        is_game_over = True
        print(f"You have lost. The correct number is {computerChoice}")

while(input("Do you want to play number guessing game? Type 'y' to continue, 'n' to exit").lower() =='y'):
   os.system('cls' if os.name == 'nt' else 'clear')
   play_game()