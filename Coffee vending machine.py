menu = {
    "espresso" : 
        {"ingredients" :
            {"water" : 50 , "coffee" : 18},"cost" : 1.5
        },
    "latte" : 
        {"ingredients" : 
            {"water" : 200 , "milk" : 150 , "coffee" : 24},
            "cost" : 2.5
        },
    "cappuccino" : 
        {"ingredients" : {"water" : 250, "milk" : 100 ,"coffee" :24,}, "cost" : 3.0}
}

def check_resources(required_resources):
    """checks whether there are sufficient resources available to process"""
    for item in required_resources:
        if required_resources[item] >= resources[item]:
            print(f"Sorry there is not enough {resources}.")
            return False
    return True

def process_coins():
    """process coins and calculate the value"""
    quarters = int(input("Enter the no. of quarters :"))*0.25
    dimes = int(input("Enter the no. of dimes :"))*0.10
    nickels = int(input("Enter the no. of nickels :"))*0.05
    pennies = int(input("Enter the no. of pennies :"))*0.01
    inserted_money = quarters + dimes + nickels + pennies
    if inserted_money >= menu[choice]['cost']:
        change = inserted_money - menu[choice]['cost']
        print(f"Your change is: {change:.2f}$")
        
        
    elif inserted_money < menu[choice]['cost']:
        print("Sorry that's not enough money. Money refunded.")


profit = 0
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
    }


prompt = True

while prompt:
    choice = input("“What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        prompt = False
        break
    elif choice == "report":
        print(f"Resources available are: water:\n {resources['water']}ml,\n milk: {resources['milk']}ml, \n coffee: {resources['coffee']}g,\n money: {profit}$")
    else:
        check_resources(menu[choice]["ingredients"])
        process_coins()
        for item in menu[choice]['ingredients']:
            resources[item] -= menu[choice]['ingredients'][item]
            profit += menu[choice]['cost']
    print(f"Here is your {choice}. Enjoy")

