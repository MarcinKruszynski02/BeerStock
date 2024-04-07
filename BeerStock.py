import Modules
TYSKIE = 1
CARLSBERG = 2
SOMERSBY = 3
REDS = 4
OKOCIM = 5
BOSMAN = 6
LECH = 7
EXIT = 0

beerMap = {TYSKIE: 'Tyskie', CARLSBERG: 'Carlsberg', SOMERSBY: 'Somersby', REDS: 'Reds', OKOCIM: "Okocim", BOSMAN: "Bosman", LECH: "Lech"}
priceMap = {TYSKIE: 1.5, CARLSBERG: 2.1, SOMERSBY: 4.3, REDS: 3.5, OKOCIM: 1, BOSMAN: 3.2, LECH: 3.5, EXIT: 0}

ownedBeer = []
namesOfOwnedBeer = []

money = 30

def ListOfBeerToTxt():
        with open("yourBeers.txt","w") as plik:
                for i, element in enumerate(ownedBeer):
                    namesOfOwnedBeer = beerMap.get(element)
                    plik.write(namesOfOwnedBeer)
                    if i != len(ownedBeer) -1:
                        plik.write('\n')
        print("Your bers was saved to file")
def DisplayBeer():
     print("Your beers is:")
     for element in ownedBeer:
        namesOfOwnedBeer = beerMap.get(element)
        print(namesOfOwnedBeer)

def ModifyMoneyForBuy(beer):
    global money
    money -= beer
    
def ModifyMoneyForSell(beer):
    global money
    money += beer
       
def DisplayBeerMenu():
    print(f'1 -- Tyskie price: {priceMap[TYSKIE]}$')
    print(f'2 -- Carlsberg price: {priceMap[CARLSBERG]}$') 
    print(f'3 -- Somersby price: {priceMap[SOMERSBY]}$') 
    print(f'4 -- Reds price: {priceMap[REDS]}$') 
    print(f'5 -- Okocim price: {priceMap[OKOCIM]}$') 
    print(f'6 -- Bosman price: {priceMap[BOSMAN]}$') 
    print(f'7 -- Lech price: {priceMap[LECH]}$') 

def BuyBeer():
        DisplayBeerMenu()
        id = int(input("enter number: "))
        isExist = beerMap.get(id)
        if(isExist): 
            if(money >= priceMap[id]):
                print(f"You bought {beerMap[id]}!!")
                ModifyMoneyForBuy(priceMap[id])
                ownedBeer.append(id)
            else: print("You don't have enough money!")
        else:
             print("An invalid value has been entered. A digit between 1 and 9 is required.")   

def sellBeer():
        DisplayBeerMenu()
        id = int(input("enter number: "))
        isExist = beerMap.get(id)
        hasOwned = id in ownedBeer
        if(isExist): 
             if hasOwned:
                print(f"You sold {beerMap[id]}")
                ModifyMoneyForSell(priceMap[id])
                ownedBeer.remove(id)
             else:
                print("You don't have this beer")   
        else:
             print("An invalid value has been entered. A digit between 1 and 9 is required.")

while True:
    try:    
        Modules.Menu(money)
        userInput = int(input("enter number: "))
        if userInput == 1:
            BuyBeer()
        elif userInput == 2:
            sellBeer()
        elif userInput == 3:
            if not ownedBeer:
                print("You don't have any beers time to buy some %!")
            else:
                DisplayBeer()
            if money == 0: 
                print("You don't have money") 
        elif userInput == 4:
            ListOfBeerToTxt()      
        elif userInput == 0:
            print("Exit")
            break
        else:
            print("there is no such digit from the menu! click any digit to return to the menu")
            liczbaUzytkownika = int(input(""))
        print("") 
    except ValueError as e:
        print("An invalid value has been entered. A digit between 1 and 7 is required.")
            
