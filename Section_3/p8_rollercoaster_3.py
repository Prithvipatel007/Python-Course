print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if(height > 120):
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if(age <= 12):
        bill = 20
        print(f"Child tickets are Rs {bill}")
    elif(age <= 18):
        bill = 50
        print(f"Youth tickets are Rs {bill}")
    elif(age >= 45 and age <= 55):
        bill = 0
        print(f"Your tickets will be free")
    else:
        bill = 100
        print(f"Adult tickets are Rs {bill}")

    want_photo = input("Do you want a photo taken? Y or N : ")
    if(want_photo == "Y" or want_photo == "y"):
        bill += 50

    print(f"Your total bill is Rs {bill}")
else:
    print("You cannot ride the rollercoaster")