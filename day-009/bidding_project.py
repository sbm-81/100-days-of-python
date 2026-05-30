logo = r'''
                        ___________
                        \         /
                         )_______(

                         |"""""""|_.-._,.---------.,_.-._
                         |       | | |               | | ''-.
                         |       |_| |_             _| |_..-'
                         |_______| '-' `\'---------\'` '-'
                         )_______(
                        /_________\
                       .-----------.
                      /_____________\
'''

print(logo)

ask="yes"
bidders={}
hisghest_bidder=''
highest_bid=0
while ask!="no":
    name=input("What is your name? \n")
    bid=int(input("What is your bid? \n$"))
    bidders[name]=bid
    if bid>highest_bid:
        highest_bid=bid
        hisghest_bidder=name
    ask=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if ask=="yes":
        print("\033c", end="")

print(f"The winner is {hisghest_bidder} with a bid of ${highest_bid}.")
