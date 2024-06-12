import time

iron = 0
hp = 20
merchantitems = ['Stone Sword', 'Iron Sword', 'Diamond Sword', 'Chainmail Armor', 'Iron Armor', 'Diamond Armor']
youritems = []

print("Choose your team from below:")
time.sleep(0.25)
print("Red")
time.sleep(0.25)
print("Blue")
time.sleep(0.25)
print("Green")
time.sleep(0.25)
print("Yellow")
time.sleep(0.25)
team = input("Enter your choice: ")
currently_doing = "Generator"
def nextMsg():
    time.sleep(0.25)
    print("What would you like to do next?")
    time.sleep(0.25)
    print("Here are your choices:")
    time.sleep(0.25)
    print("Go to the Merchant")
    time.sleep(0.25)
    print("PVP a player")
    time.sleep(0.25)
    print("Attempt to Break a Bed")
    time.sleep(0.25)
    print("Go to the Generator")
def nextAction(action):
    global currently_doing
    if action.lower() == "go to the merchant":
        currently_doing = "Merchant"
    elif action.lower() == "pvp a player":
        currently_doing = "PVP"
    elif action.lower() == "attempt to break a bed":
        currently_doing = "Break Bed"
    elif action.lower() == "go in generator":
        currently_doing = "Generator"
    time.sleep(2)
    if currently_doing == "Merchant":
        merchant()
    elif currently_doing == "PVP":
        pvp()
    elif currently_doing == "Break Bed":
        breakbed()
    elif currently_doing == "Generator":
        generator()

def merchant():
    global merchantitems
    print("Welcome to the merchant!")
    print("Here, you can buy all the necessary tools to survive!")
    print("Here are my available items:")
    for item in merchantitems:
        print(item)
        time.sleep(0.25)
    while True:
        try:
            buyitem = input("Would you like to buy anything? Y/N: ")
            if buyitem.lower() == 'y':
                buy = input("What would you like to buy? Put the full name of the item. (Case Sensitive): ")
                merchantitems.remove(buy)
                youritems.append(buy)
                print(f"You have bought: {buy}")
        except ValueError:
            print("Sorry, but the item you want to buy is not available. Please check your spelling. (All items are case-sensitive)")

def pvp():
    print("Lets PVP!")

def breakbed():
    print("Lets go break a bed!")

def generator():
    global iron
    print("You are in the generator!")
    print(f"You currently have {iron} iron.")
    time.sleep(5)
    iron += 15
    print(f"You now have {iron} iron.")
    nextMsg()
    action = input()
    nextAction(action.lower())
nextAction("generator")
