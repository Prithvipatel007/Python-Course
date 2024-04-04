print("Welcome to Pizza Deliveries!")
size = input("Which pizza size would you prefer? S, M or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")

bill = 0

if(size == "S"):
    bill += 100
elif(size == "M"):
    bill += 200
elif(size == "L"):
    bill += 300
else:
    print("Invalid input")

if(add_pepperoni == "Y"):
    if(size == "S"):
      bill += 10
    else:
      bill += 20

if(extra_cheese == "Y"):
   bill += 10

if(bill > 0):
  message = f"Your final bill is Rs {bill}"
  print(message)