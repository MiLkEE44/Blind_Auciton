# I didn't use functions in the version that I made; this was taken from 
# Angela Yu's Finished project course and here for me to have quick access to 
# and review 

# This just replaces the highest number in the highest bid and the name tied 
# to that number from the dictionary is declared the winner. 
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

# The dictionary containing the values from the inputs outside the while loop
# While more bidders say "yes" they keep answering the inputs and get added to the dict
# The loop ends when they say "no" and the function gets called to find the highest bidder. 
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? TYpe 'Yes' or 'No'. \n").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 100)
