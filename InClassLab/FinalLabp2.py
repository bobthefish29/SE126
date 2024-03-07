#david punchak
#SE126 
#Lab 9 "Final lab"



####################------Notes-------###############

#I got this working, some how


###################----------------Project discription-----------------###################
'''
Write a program that can be used by a small theater to sell tickets for performances.

The theaters auditorium has 15 rows of seats with 30 seats in each row. 

The program should display a screen that shows which seats are available and which are taken. 

Seats that are available are represented by # and seats that are taken are represent by a *.

There are aisles after seats H and V.
'''




#importing for the clear function
from os import system, name 

#####################--------Setting the vars-------#############
rowList = ["#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#"]
seatRow = ["A","B","C","D","E","F","G","H"," ","I","J","K","L","M","N","O","P","Q","R","S","T","U","V"," ","W","X","Y","Z","1","2","3","4"]
count = 0
fullList = []
userInput = 0
totalPrice = 0
totalSeatSold = 0
totalSeatSoldList = []
ifSeatTakenTotal = 0
currentUserList = []
currentUserPrice = 0


#making a full list
while count != 15:
    #dylan added the .copy() no idea it was a thing
    fullList.append(rowList.copy())
    count += 1

############------Functions-------##############3

#just a clear
def clear():

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

#this is the display for the seating view
def display():
    #setting vars for the counts
    displayCount = 0
    L = 0
    
    #just printing text
    print("Row\t\t\t\t\t\tSeats")
    print(f"      {seatRow}")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    #this what is displaying the list
    while displayCount != 15:

        #for i in range(0, len(fullList[L])):
        print(f"{L + 1:3}   {fullList[L]}")

        displayCount += 1
        L += 1
    
    #this is just returning fulllist, i dont know if i could just remove this and be fine
    return fullList

#the menu for the program
def menu():
    #only reply the user can do is 1,2,3,4,5
    menuOnly = [1,2,3,4,5]
    #texts
    print("\t----What would you like to do user?---")
    print("\n1. Buy a seat")
    print("2. View total sales")
    print("3. View Sales Information")
    print("4. Check Out")
    print("5. Exit")

    #could be dealeted but i dont want to try
    #This is trying the input as an int if its not it ask the user to pick again
    try:
        userInput = int(input("What would you like to do user: "))
    except:
        print("\n\n\t\t----Enter a number----\n\n")
        clear()
        return menu()
    #when the user puts in a number it would pass the try but if its to bit it would brake, thats why this is here

    while userInput not in menuOnly:
        #asking for a number 1-5
        print("\n\t\tA number [1-5]!!!!\n")
        #trying the same input but now when the number is 
        try:
            userInput = int(input("What would you like to do user: "))
        except:
            print("\n\t\t----It has to be a number 1-5 user.---STOP---!!!")
    #just a clear
    clear()
    return userInput

#this is getting the function for the user row input
def userRowInput():
    #setting a var 
    userInputRow = - 1

    #this is just to ceatch the user to enter a row 1-15 and if not it asks for a number
    while userInputRow < 1 or userInputRow > 15:
            try:
                userInputRow = int(input("\nPlease enter a Row (1-15): "))
            except:
                print("Invalid integer, enter a number!")
            if userInputRow >= 1 and userInputRow <= 15:
                return userInputRow
            else:
                print("A number 1-15")


    #this is returning the number value the user inputs that is 1-15
    return userInputRow

#the same as getting row, this time its for the seat
def userSeatInput():
    #asking for a letter or number than setting it to upper case, if the user does not enter a correct value they will be stuck in the loop
    try:
        userInputSeat = str(input("\nPlease enter a Seat A-Z or 1,2,3,4: ")).upper()
    except:
        print("Invalid integer, enter a number!")
    
    while userInputSeat not in seatRow:
        
        try:
            print("\t---Error")
            userInputSeat = str(input("\nPlease Enter[A-Z or 1-4]: ")).upper()
        except:
            print("Invalid Entry")




    #returning the user input value
    return userInputSeat


#################------------God i dont know how this works-----------############

#the function for setting the value to the correct location in the map, than it also is doing the math for the seat, and 
def IfItWorks(userRow, userSeat, totalPrice, totalSeatSold, totalSeatSoldList, currentUserPrice ):
    
    

    #Setting a lot of local vars for the function
    copyList = fullList
    copyTotalPrice = totalPrice
    copySeatSold = totalSeatSold
    copytotalSeatSoldList = totalSeatSoldList
    row = userRow - 1
    seat = userSeat
    foundAt = 0

    #this is for looking for the index the letter is at, the lists are the same so the value is also the same in the main list
    for i in range(0, len(seatRow)):
        if seat == seatRow[i]:
            foundAt = i
    
    #this is if the row, and the letter index is a value it could not be than it puts the user back in the menu, if no than its adding the value 
    if copyList[row][foundAt] == "*":
        print("\n\n\t\t------Sorry Seat Taken-------")
        input("\n\t\t-----Press Enter To return-----")
        return copyList, copyTotalPrice, copySeatSold, copytotalSeatSoldList, currentUserPrice
    else:
        #setting it to the location
        copyList[row][foundAt] = "*"
        row += 1

        #this is setting it to a total list and a user list for latter displays
        copytotalSeatSoldList.append([row,seat])
        currentUserList.append([row,seat])
        print("\n---The seat is open---")
        
        #this is the math for price.
        if row < 5:
            
            copyTotalPrice += 200
            currentUserPrice += 200
        elif row >= 6 and row <= 10:
            #print("Between 6-10")
            #print(row)
            copyTotalPrice += 175
            currentUserPrice += 175
        else:
            #print("Grater than 10")
            #print(row)
            copyTotalPrice += 150
            currentUserPrice += 150
    
    input(f"\n\t---Enter to add to cart---")


    #this is just for the total numebr of seats sold
    copySeatSold +=1

    return copyList, copyTotalPrice, copySeatSold, copytotalSeatSoldList, currentUserPrice

#################------------Same with this one-----------############

#this is for the sails information
def sailsInformation():
    #this is setting vars, need testing list
    testingList = []
    ifSeatTaken = 0
    totalSeatLeft = 0

    #this is running though each list than running rhought each data in said list
    #this is running 15 times V
    for r in range (0, len(fullList)):
        #this is running 32 times V
        for s in range(0, len(fullList[r])):
            #this is running 480 times V
            totalSeatLeft += 1
            #this is to see if the item in that location is a * than it does nothing, but add one to seats taken
            if fullList[r][s] == "*":
                ifSeatTaken += 1
            elif fullList[r][s] == " ":
                totalSeatLeft -= 1
            else:
                #this is append the value to the row with the number of seats, so row 1 would have 30 seats if nun were bought
                testingList.append([r + 1,s + 1])
    
    #this was the only way i could think to do it, its each row than getting the value
    i = 0
    row1 = 0
    row2 = 0
    row3 = 0
    row4 = 0
    row5 = 0
    row6 = 0
    row7 = 0
    row8 = 0
    row9 = 0
    row10 = 0
    row11 = 0
    row12 = 0
    row13 = 0
    row14 = 0
    row15 = 0
    #this is running for a long time and adding the value to the lsit
    for i in range(0, len(testingList)):

        #if the value is a 1 than it adds 1 to the count of seats in row 1 that is oppen and so on
        if testingList[i][0] == 1:
            row1 += 1
        elif testingList[i][0] == 2:
            row2 += 1
        elif testingList[i][0] == 3:
            row3 += 1
        elif testingList[i][0] == 4:
            row4 += 1
        elif testingList[i][0] == 5:
            row5 += 1
        elif testingList[i][0] == 6:
            row6 += 1
        elif testingList[i][0] == 7:
            row7 += 1
        elif testingList[i][0] == 8:
            row8 += 1
        elif testingList[i][0] == 9:
            row9 += 1
        elif testingList[i][0] == 10:
            row10 += 1
        elif testingList[i][0] == 11:
            row11 += 1
        elif testingList[i][0] == 12:
            row12 += 1
        elif testingList[i][0] == 13:
            row13 += 1
        elif testingList[i][0] == 14:
            row14 += 1
        else:
            row15 += 1
        
    #This is appending each value that was found to there list into one final list for the display
    finalList = []
    finalList.append([1, row1])
    finalList.append([2, row2])
    finalList.append([3, row3])
    finalList.append([4, row4])
    finalList.append([5, row5])
    finalList.append([6, row6])
    finalList.append([7, row7])
    finalList.append([8, row8])
    finalList.append([9, row9])
    finalList.append([10, row10])
    finalList.append([11, row11])
    finalList.append([12, row12])
    finalList.append([13, row13])
    finalList.append([14, row14])
    finalList.append([15, row15])
    


    #the math to take away seats thagt were not open
    totalSeatLeft -= ifSeatTaken
    
    #just a display for how many seats are open for not
    print("Row\t   Seat")
    print("------------------------------------------------")
    for p in range(0, len(finalList)):

        print(f"Row {p + 1:3}: {finalList[p][1]} seats")
    print(f"\nThere are {totalSeatLeft} seats left ")
    print(f"There were {ifSeatTaken} seats taken")
    input("\n\n\t---------Enter to go back---------")
    #clearing
    clear()
    return ifSeatTaken
            
#this is for the checkout 
def checkOut(currentUserList, currentUserPrice):
    
    #welcome print
    print("\t\t-------------Welcome to check out----------")

    print("\n\nYou are buying:\n")
    #this is for each seat and row to be displayed
    for i in range(0, len(currentUserList)):
        print(f"Row: {currentUserList[i][0]} Seat: {currentUserList[i][1]} ")
    
    
    print(f"\nThe price somes to: ${currentUserPrice}")


    input("\n\t\t------Press enter to buy-------")
    #setting the vlaues to 0 so a different user can use it
    currentUserList = []
    currentUserPrice = 0
    
    return currentUserList, currentUserPrice



#-----------------------Main code--------------------------------------

print("\t\t------Welcome to the seating proream-----------\n\n")

while userInput != 5:
    #seeing the menu
    userInput = menu()
    #if the user reply is the value than it does whay it is
    if userInput == 1:

        #calling the different functions
        fullList = display()
        userRow = userRowInput()
        userSeat = userSeatInput()
        fullList, totalPrice, totalSeatSold, totalSeatSoldList, currentUserPrice = IfItWorks(userRow, userSeat, totalPrice, totalSeatSold, totalSeatSoldList, currentUserPrice)
        clear()
    elif userInput == 2:
        
        print("\n\n\t-----------Total Ticket sales------------")
        print(f"\n\tYou have sold a total of {totalSeatSold} seats")
        print(f"\tThe total price somes to: ${totalPrice}")
        input("\n\n\t----------Press Enter To go back------------")
        clear()

    elif userInput == 3:
        #print(totalSeatSoldList)
        ifSeatTakenTotal =+ sailsInformation()
        
    elif userInput == 4:
        #print(currentUserList)

        currentUserList, currentUserPrice = checkOut(currentUserList, currentUserPrice)
        clear()

    else:
        print("--Thank you for using my program :)--")
        input("\n\n\t-----Press Enter to quit----")
############################-------------------End of the project-----------------###################