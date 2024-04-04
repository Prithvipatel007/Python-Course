# store states of india

states_of_india = [ "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
                   "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", 
                   "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", 
                   "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
                   "Uttar Pradesh", "Uttarakhand", "West Bengal"]

print(states_of_india[1])

#alter any value in the list
states_of_india[0] = "AndhraPradesh"
print(states_of_india)

# add item at the end of the list
states_of_india.append("SomethingPradesh")
print(states_of_india)

# index out of range error
states_of_india[100]