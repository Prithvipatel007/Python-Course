programming_directory = {
    "Bug":"An error in a program that prevents the programs from running as expected.",
    "Function" : "A piece of code that you can call over and over again."
}
#print(programming_directory)

# retrieve an item from the list
# make sure the key is in a string datatype
#print(programming_directory["Bug"])  # spell the key correctly

# add new item to dictionary
programming_directory["Loop"] = "The action of doing something over and over again"

#print(programming_directory)

# empty dictionary
empty_dict = {}  # empty dictionary
empty_list = []  # empty list

# clear an existing dictionary
#programming_directory = {}

#print(programming_directory)

# Edit an item in dictionary
programming_directory["Bug"] = "A moth in your computer"

print(programming_directory)

# loop through dictionary
for key in programming_directory:
    print(key)
    print(programming_directory[key]) # gives the value of the key

# Nesting 
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# Nesting a list in a dictionary - Where have I already traveled?
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting dictionary in a dictionary - Label the list of data
travel_log = {
    "France" : { "cities_visited" :  ["Paris", "Lille", "Dijon"], "total_visits" : 12},
    "Germany" : { "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 15}  # challenge!
}

# Nesting a dictionary in a list
travel_log = [
    {
        "Country": "France", 
        "cities_visited" :  ["Paris", "Lille", "Dijon"], 
        "total_visits" : 12
    },
    {
        "Country": "Germany", 
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits" : 15
    }
]

