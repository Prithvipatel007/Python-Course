import random
from common import logo
import os

def deal_card():
    """
    Returns a random card from the list of cards
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    Returns a list of cards and returns the sum of cards
     * If the sum is 21(has a 10 and 11 in it) and its only two cards, then the sum is 0
     * If the sum is over 21 and there is 11 in the list of cards, use 1 instead of 11
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if(11 in cards and sum(cards) > 21):
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare (user_score, computer_score):
    """
    Compare user and computer score and distinguish whether the user wins or loses
    """
    if (user_score == computer_score):
        return "Draw"
    elif (computer_score == 0):
        return "You have lost, the opponent has blackjack"
    elif (user_score == 0):
        return "Win with a Blackjack"
    elif (user_score > 21):
        return " You went over. You lose"
    elif (computer_score > 21):
        return " Opponent went over. You win"
    elif (user_score > computer_score):
        return "You win"
    else:
        return "You lose"

def play_game():

  print(logo)
  
  user_cards = []
  computer_cards = []

  is_game_over = False

  for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())

  while(not is_game_over):
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f" Your cards : {user_cards} and current score: {user_score}")
    print(f" Computer Card : {computer_cards[0]}")

    if(user_score == 0 or computer_score == 0 or user_score > 21):
        is_game_over = True
    else:
        user_should_deal = input(" Type 'y' to get another card, type 'n' to stand : ").lower()
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

  while (computer_score != 0 and computer_score < 17):
      computer_cards.append(deal_card())    
      computer_score = calculate_score(computer_cards)

  print(f"Your final hand is {user_cards} and your final score is {user_score}")
  print(f"Computer's final hand is {computer_cards} and computer final score is {computer_score}")

  print(compare(user_score, computer_score))

while (input("Do you want to play again? Type 'y' or 'n' : ") == "y"):
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()