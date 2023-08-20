#Review:
# Create a function called greet()
# Write 3 print statements inside the function
# Call the greet() function and run your code

# def greet():
#     print("Greetings")
#     print("Greetings")
#     print("Greetings")

# greet()

# functions that allows input to pass

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")

# name = input("What is your name?")
# greet_with_name(name)

#functions with multiple inputs

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

#Positional Argument
#greet_with("Prithvi", "Ahmedabad")
#greet_with("Ahmedabad", "Prithvi")

# Keyword argument
greet_with(
    name="Prithvi",
    location="Ahmedabad"
)