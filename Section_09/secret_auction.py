from common import logo
import os

end_bidding = False
bids_log = {}

def add_bid(name, bid):
    bids_log[name] = bid

def find_highest_bid():
    max = 0
    maxName = ""
    for person in bids_log:
        if(bids_log[person] > max):
            max = bids_log[person]
            maxName = person
    
    print(f"The highest bidder is {maxName} with the bid of Rs. {max}")

while(end_bidding != True):
    print(logo)
    name = input("What is your name? ")
    bid = int(input("What is your bid? Rs. "))
    add_bid(name, bid)

    ans = input("Are there any other bidder? Type Yes if there is else No : ").lower()
    if(ans == "yes"):
        end_bidding = False
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        end_bidding = True
        find_highest_bid()

