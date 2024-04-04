#input: 156 178 165 171 187
#input: 156 178 165 171 187 172 185

"""
Convert student heights from string to int values
"""
student_heights = input("Input a list of student heights ").split(" ")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum = 0
length = 0
average = 0

for n in student_heights:
    sum += n 
    length = length + 1

average = sum / length

print(f"Average : {average}")