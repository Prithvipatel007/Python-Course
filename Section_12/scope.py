#enemies = 1
#
#def increase_enemies():
#    enemies = 2
#    print(f"enemies inside function {enemies}")
#
#increase_enemies()
#print(f"enemies outside function {enemies}")

# Local scope

# def drink_potion():
#    ## potion_strength is only available within the function
#    potion_strength = 2
#    print(potion_strength)
#
#drink_potion(potion_strength) # gives an error

# Global scope
# 
# player_health = 10
# 
# def drink_potion_g():
#   print(player_health)
#     
# drink_potion_g()

# There is no block scope

game_level = 3
enemies = ["skeleton", "Zombies", "Aliens"]

## This works
#if(game_level < 5):
#  new_enemy = enemies[0]
#
#print(new_enemy)

# This doesnot
# def create_enemy():
#  if(game_level < 5):
#    new_enemy = enemies[0]
#
#print(new_enemy)
#

# Modifying Global Scope
# enemies = 1  # avoid modifying global variables

# def increase_enemies(): 
#     enemies += 1   # creates new var with local scope
#     print(f"enemies inside function {enemies}")
# 
# increase_enemies()
# print(f"enemies outside function {enemies}")

# Global constants
# make all global variables to upper case

PI = 3.1415
URL = "https://google.com"

#You easily know whether it is a global variable or not