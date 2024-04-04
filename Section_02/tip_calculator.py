print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? Rs "))
tip_percent = int(input("What percentage tip would you like to give? 10%, 12%, or 15%? "))
people = int(input("How many people to split the bill? "))
pay_per_person = 0

total_bill_with_tip = (total_bill * (12/100)) + total_bill
pay_per_person = round(total_bill_with_tip / people, 2)

pay_per_person_format = "{:.2f}".format(pay_per_person)

message = f"Each person should pay: {pay_per_person_format}"
print(message) 