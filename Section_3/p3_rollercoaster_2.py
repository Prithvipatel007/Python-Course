print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if(height > 120):
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if(age <= 12):
        print("Please pay Rs 20")
    elif(age <= 18):
        print("Please pay Rs 50")
    else:
        print("Please pay Rs 100")
else:
    print("You cannot ride the rollercoaster")