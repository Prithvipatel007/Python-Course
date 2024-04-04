import random

random_integer = random.randint(1,10)
print(str(random_integer)) 

# 0.0000000 to 0.99999999
random_float = random.random()
random_float  = random_float * 5.0
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")