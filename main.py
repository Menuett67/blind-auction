from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("welcome to secret auction program.")
def max_of_bids(users_bids):
  max=0
  winner=""
  for person in users_bids:
    bid_amount=int(users_bids[person])
    if bid_amount>max:
      max=bid_amount
      winner=person
  print(f"the winner is {winner} with a bid of {max}.")
finish=False
bidders={}
while not finish:
  name=input("what is your name?")
  price=input("what is your bid ?$")
  bidders[name]=price
  should_continue=input("are there any other bidders?Type'yes' or 'no'.")
  if should_continue=="no":
    finish=True
    max_of_bids(bidders)
  elif should_continue=="yes":
    clear()

    
    
