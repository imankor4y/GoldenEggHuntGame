import time
import math
import random

classTypes = ["Lyra Stormwhisper", "Rowan Ironbrand", "Elowen Brightquill"]
statNames = ["Strength:", "Agility:", "Intelligence:", "Perception:", "Endurance:"]
classStats = [[4,8,3,8,5], [8,3,2,5,8], [2,3,9,7,4]]
pName = ""
pStats = [0,0,0,0,0]
statAdjustment = [0,0,0,0,0]
pClass = -1
pMoney = 500
pStatus = "Fine"
pLevel = 0
pExp = 0
currentLocation = "Abandoned Campsite"
placesToTravel = [["Golden Nest", "Dense Forest", "Crashed Alien Pod", "Thicket", "Streambank", "Abandoned Campsite"],[400,300,200,100,75,0]]
distanceToHome = 0
activityMenu = ["View Stats", "Travel", "Shop", "Inventory"]
itemsToBuy = [["potion", "burnHeal", "iceHeal", "statBoost", "cheapVase", "expensiveVase", "garbage"],[100, 50, 50, 200, 25, 300, 0]]
inventory = ["potion"]


def indexInList(item, myList):
    foundIndex = -1
    for i in range(len(myList)):
        if item == myList[i]:
            foundIndex = i
            break
    return foundIndex


def listToText(myList):
    combinedText = "\n"
    for i in range(len(myList)):
        combinedText = combinedText + str(i) + ") " + myList[i] + "\n"
    return combinedText


def checkMenuRange(question, listName, isCancelable=False):
    while True:
        user_input = input(question + listToText(listName))
        try:
            index = int(user_input)
            if isCancelable and index == -1:
                return index
            if 0 <= index < len(listName):
                return index
            else:
                print("Invalid choice, please enter a number from the list.")
        except ValueError:
            print("Invalid input, please enter a number.")


def starLine(numRows, numSleep):
    sLine = "*" * 10
    for i in range(numRows):
        print(sLine)
    time.sleep(numSleep)


print("Welcome to the Golden Egg Hunt!")
starLine(3, 1)

print("Choose your Character")
starLine(2, 2)

for i in range(len(classTypes)):
    print(classTypes[i] + ":")
    for j in range(len(classStats[i])):
        print(statNames[j], classStats[i][j])
    starLine(1, 1.5)

pClass = checkMenuRange("Enter the number associated with your chosen character: ", classTypes)

pName = classTypes[pClass]
pStats = classStats[pClass]

print("You have chosen " + pName + "!")
starLine(2, 2)

print("You are now known as " + pName)
starLine(1, 3)

print("Long ago, in a forgotten age, the Golden Egg was hidden deep within a hostile forest.")
starLine(1, 6)

