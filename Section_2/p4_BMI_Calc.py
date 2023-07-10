weight = input("Please write your weight in Kg : ")
height = input("Please write your height in m : ")

result = float(weight) / float(height)**2
bmi_as_int = int(result)
print("The result is : " + str(bmi_as_int))