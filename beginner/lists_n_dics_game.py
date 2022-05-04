#inventory as dictionary
"""inventory = {
     "gp" : 0,
     "sword" : "bronze sword",
     "shield" : "bronze shield",
     "runes" : ["air", "water", "mind", "earth"]
}
inventory["runes"].append("body")
inventory["runes"].remove("air")
inventory["runes"].sort()
print(f'gold: {inventory["gp"]}')"""

# inventory as a list
inventory2 = ["bronze scimitar"]

# drops an item
def drop(x):
    inventory2.remove(x)
    return inventory2

#p picks up an item
def pickup(x):
    inventory2.append(x)
    return inventory2

"""how do i add another oak log and make it say "2 oak logs"?
how do i count the number of times something is repeated in a list?"""

# counts number of times an item is repeated in a list
def count_item(y, x):
    return y.count(x)

# bank list
bank = []

# deposits item to the bank
def bank_deposit(x):
    inventory2.remove(x)
    bank.append(x)
    return

# withdraws item from bank
def bank_withdraw(x):
    bank.remove(x)
    inventory2.append(x)
    return

# list of actions for the user
actionslist = ["chop trees", "bank", "logout", "fight"]

while True:
    # asks what the user would like to do
    action = input(f'What would you like to do? {actionslist} ')

    if action == "chop trees":
        # chop the oak tree
        chopn = int(input("How many times are you choppin' the oak tree? "))

        # chops the oak tree how many times the user requests 
        while chopn >=1:
            chopn = chopn - 1
            pickup("oak log")

        """for x in range(chopn):
            pickup("oak log")
            print(x)"""

        # tells you how many oak logs are in your inventory    
        print(f'You now have {count_item(inventory2, "oak log")} oak logs')

    elif action == "bank":
        # add withdraw option to the bank
        bankchoicelist = ["deposit", "withdraw"]

        bankchoice = input(f'What would you like to do? {bankchoicelist} ')
        if bankchoice == "deposit":

            """asks user which item and how many of it to deposit, still have to make bank_deposit() multiply by deposit_item_amount
            print entire inventory but like nicely
            print(f'inventory: {count_item(inventory2, "oak log")} oak logs ')
            figure out how to make duplicate items not get counted
            set of inventory2 only counts the uniques in the list! amazing"""
            
            for x in set(inventory2):
                # adds an s to plurals, not good for plurals not ending in s
                if count_item(inventory2, x) != 1:
                    print(f'{count_item(inventory2, x)} {x}s')
                else:
                    print(f'{count_item(inventory2, x)} {x}')

            # user decides what to deposit
            # TODO somehow make plural of deposit_item acceptable?
            deposit_item = input("What would you like to deposit? ")
            deposit_item_amount = int(input("How many would you like to deposit? "))

        

            # deposits the item how many times the user requests
            while deposit_item_amount >=1:
                deposit_item_amount = deposit_item_amount - 1
                bank_deposit(deposit_item) 

        elif bankchoice == "withdraw":

            for x in set(bank):
                # adds an s to plurals, not good for plurals not ending in s
                if count_item(bank, x) != 1:
                    print(f'{count_item(bank, x)} {x}s')
                else:
                    print(f'{count_item(bank, x)} {x}') 

            # user decides what to withdraw
            withdraw_item = input("What would you like to withdraw? ")

            # if theres only 1 item, doesn't ask how many to take out
            if count_item(bank, x) == 1:
                withdraw_item_amount = 1
                pass
            else:
                withdraw_item_amount = int(input("How many would you like to withdraw? "))

            # withdraws the item how many times the user requests
            while withdraw_item_amount >=1:
                withdraw_item_amount = withdraw_item_amount - 1
                bank_withdraw(withdraw_item)

        """fix it so that oak logs gets replaced with x, also make sure to print every item in bank. for loop?"""
        for x in set(bank):
            # adds an s to plurals, not good for plurals not ending in s
            if count_item(bank, x) != 1:
                print(f'Your bank now contains {count_item(bank, x)} {x}s')
            else:
                print(f'Your bank now contains {count_item(bank, x)} {x}')
    # TODO add a combat system???

    elif action == "logout":
        print("See you next time!")
        break