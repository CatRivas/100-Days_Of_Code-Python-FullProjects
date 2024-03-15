from art import logo
import os

def clear_screen():
    # Windows
    os.system('cls')

print(logo)

#empty dictionary for all the bidders
bids = {}

#this just saves all the bids
def add_bid(bidder_name, bidder_bid):
    bids[bidder_name] = bidder_bid

#looking for the winner
def get_highest_bid(dict_bids):
    highest_bid = 0
    highest_name = ''

    for key_name in dict_bids:
        bid_value = dict_bids[key_name]
        if bid_value > highest_bid:
            highest_bid = bid_value
            highest_name = key_name    

    print(f'The winner is {highest_name} with a bid of ${highest_bid}')


#user inputs 
def get_inputs():    
    while True:
        name = input('What is your name?: ').strip().title()
        bid = int(input("What's your bid?: $" ).strip())

        add_bid(name, bid)


        play = input("Are there any other bidders? Type 'yes' or 'no'\n")

        if play == 'no':
            clear_screen()
            get_highest_bid(bids)
            break
        elif play == 'yes':
            clear_screen()
        else:
            print('invalid input')
            break  


get_inputs()



