from common import logo
from common import data
from common import vs
import os
import random

def format_data(account):
  """format the game data into printable format"""
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]

  return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """ Take the user guess and follower counts and return if they got it right """
  if(a_followers > b_followers):
    return guess == "a"   # returns true if guess is a else false
  else:
    return guess == "b"

# Display art

game_should_continue = True
score = 0

account_b = random.choice(data)

# Make the game repeatable
while (game_should_continue):
  print(logo)
  print(f"Your current score is {score}")
  # Generate a random account from the game data
  account_a = account_b
  account_b = random.choice(data)

  while(account_a == account_b):
    account_b = random.choice(data)


  print(f" Compare A : {format_data(account_a)}")
  print(vs)
  print(f" Against B : {format_data(account_b)}")


  # Ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

  # Check if user is correct
  ## Get follower count of each account
  ## Use if statement to check if user is correct
  a_follower = account_a["follower_count"]
  b_follower = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower, b_follower)

  # Give user feedback for their guess
  # Score keeping
  if(is_correct == True):
    score += 1
    print(f"You guessed it right!!!! Your current score is {score}")
    os.system('cls' if os.name == 'nt' else 'clear')
  else:
    game_should_continue = False
    print(f"Sorry, you lost.. Try again next time. You final score is {score}")


# Making account at position B become the next account at position A

# Clear the screen between rounds