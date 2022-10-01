import os
import splashLogo

winning_bidder = ''
highest_bid = 0

#Clears the console
os.system('clear')

check_if_more_bidders = 'yes'
bidder_dict = {}

#Prints the splash screen for the Auction House
print(splashLogo.logo)

#Adds all bidders and bids to bidder_dict
while check_if_more_bidders == 'yes':
    bidder_name = input('SaWhat is your name?\n')
    bidder_bid = float(input('What is your bid?\n'))
    bidder_dict[bidder_name] = bidder_bid
    check_if_more_bidders = input('Is there anymore bidders?\n[Yes] or [No]\n')
    
    #Clears the console
    os.system('clear')

for i in bidder_dict:
    if bidder_dict[i] > highest_bid:
        highest_bid = bidder_dict[i]
        winning_bidder = i
    
#Prints all bidders and their bids
print(f'The winner bidder is {winning_bidder}, with a bid of ${highest_bid}.')