import random

name_string = "Angela, Ben, Jenny, Michael, Chloe"

people = name_string.split(", ")

num_items = len(people)

person_int = random.randint(0, num_items - 1)

print(f"{people[person_int]} will pay the bill")