#Main Loop

inGameLoop = True
while(inGameLoop and pStats[4] > 0):
    #stats, travel, shop, inventory
    actChoice = checkMenuRange("My noble hunter what would you like to do? ",activityMenu)
    if(actChoice ==0):
        print("Your Stats: ")
        for i in range(len(statNames)):
            print(statNames[i],pStats[i])
    elif(actChoice == 1):
        print("Travel")
    elif(actChoice == 2):
        while(True):
            print("Current balance is $" +str(pMoney))
            shopChoice = checkMenuRange("Welcome to my shop! My name is Fawn, how may I help you? Would you like to Buy or Sell?",["Buy","Sell","Show Inventory"], True)
            if shopChoice == -1:
                break
            elif shopChoice == 0:
                buyChoice = checkMenuRange("What would like to buy?" ,itemsToBuy[0])
                if(pMoney - itemsToBuy[1][buyChoice] >=0):
                    inventory.append(itemsToBuy[0][buyChoice])
                    pMoney-= itemsToBuy[1][buyChoice]
                else:
                    print("Sorry you can't afford " + itemsToBuy[0][buyChoice])
            elif shopChoice == 1:
                if(len(inventory) >0):
                    itemList = list(set(inventory))
                    showInventory(inventory)
                    sellChoice = checkMenuRange("What would you like to sell?", itemList)
                    if(sellChoice != -1):
                        itemsIndex = indexInList(itemList[sellChoice],itemsToFind[0])
                        sellPrice = math.floor(itemsToFind[1][itemsIndex] * .9)
                        confirmChoice = checkMenuRange("Are you sure you want to sell, our best price is " +str(sellPrice),["Yes","No"])
                        if confirmChoice == 0:
                            pMoney += sellPrice
                            inventory.remove(itemsToFind[0][itemsIndex])
                            print("Item Sold, current balance is $" +str(pMoney))
                        else:
                            print("Your loss!")
                        
                else:
                    print("Sorry you have nothing to sell!")
            elif shopChoice == 2:
                showInventory(inventory)
                
    elif(actChoice == 3):
        showInventory(inventory)
        
        
