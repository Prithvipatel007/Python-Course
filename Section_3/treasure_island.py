print("Welcome to the treasure island")
print("Your mission is to find the treasure")

print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
******************************************************************************* 

''')

ans = input("You're at a cross road. Where do you want to go? Type 'left' or 'right : ")

ans = ans.lower()

if(ans == "left"):
    ans = input("You came across an island in the middle of the lake. Would you like to wait for the boat or swim? Type 'wait' or 'swim' : ")
    ans = ans.lower()
    if(ans == "swim"):
        print("Shark ate you! Game over")
    elif(ans == "wait"):
        ans = input("You are on the island. You came across three doors red, yellow or green. which one would you pick? Type 'red' or 'yellow' or 'green' : ")
        ans = ans.lower()
        if(ans == "red"):
            print("You die due to fire. Game Over")
        elif(ans == "yellow"):
            print("You win!! You found the treasure!!!")
        elif(ans == "green"):
            print("A man with a gun shoots you and you die. Game Over!")
        else:
            print("Invalid answer. Game Over!")
    else:
        print("Invalid answer. Game Over!")
        
elif(ans == "right"):
    print("You fell into a hole. Game Over!")
else:
    print("Invalid answer. Game Over!")