import random as r

rock = ''' 
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"

'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissor = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

game_images = [rock, paper, scissor]

userChoice = int(input("What would you like to choose? Type 0 for Rock, 1 for Paper and 2 for scissors \n"))

if(userChoice >=3 or userChoice < 0):
    print("Invalid choice, you lose")
else:
    print(f" User chooses {game_images[userChoice]}")
    computerChoice = r.randint(0,2)
    print(f" Computer chooses {game_images[computerChoice]}")

    if(userChoice == 0):
        if(computerChoice == 0):
            print("Its a draw")
        elif(computerChoice == 1):
            print("You lose")
        elif(computerChoice == 2):
            print("You win")

    elif(userChoice== 1):
        if(computerChoice == 0):
            print("You win")
        elif(computerChoice == 1):
            print(" Its a draw")
        elif(computerChoice == 2):
            print("You lose")

    elif(userChoice == 2):
        if(computerChoice == 0):
            print("You lose")
        elif(computerChoice == 1):
            print("You win")
        elif(computerChoice == 2):
            print("Its Draw")

    else:
        print("Invalid choice, you lose!")


