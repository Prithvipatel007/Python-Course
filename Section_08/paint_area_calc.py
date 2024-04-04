import math

def paint_calc(height, width, coverage):
    num_cans = math.ceil((height * width) / coverage)
    print(f"The number of cans required are {num_cans}")

height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
coverage = 5

paint_calc(height = height, width = width, coverage = coverage)