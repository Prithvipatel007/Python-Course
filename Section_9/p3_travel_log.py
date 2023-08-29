#import os

travel_log = [
    {
        "Country": "France", 
        "Visits" : 12,
        "Cities" :  ["Paris", "Lille", "Dijon"], 
    },
    {
        "Country": "Germany", 
        "Visits" : 15,
        "Cities" : ["Berlin", "Hamburg", "Stuttgart"], 
    }
]

# TODO : Write a function that allows you to add new countries in your travel_log
def add_new_country(country, visits, cities):
    new_country = {}
    new_country["Country"] = country
    new_country["Visits"] = visits
    new_country["Cities"] = cities
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)
#os.system('cls' if os.name == 'nt' else 'clear')