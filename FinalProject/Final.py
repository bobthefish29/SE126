#David Punchak






#the program runs well but test run it and try to fail. sleeping got some more time but neeed a lot more for what i want. 1-2 more days for just one idea than 3 tops for final. dont have that 







##################-------------Imports------------############
import random
import csv
import time
from os import system, name 


###########----------------Setting global Vars / lists----------------##################
userMenuChoise = 0




################----------------Functions--------------##############
#just the clear function
def clear():

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

#Not done but going to be menu that just returns a int of a number 1-4 nothing else.
def menu():
    print("What would you like to do user")
    print("1. play maze")
    print("2. veiw score board")
    print("3. view map layout.")
    print("4. leave")



    userInput = int(input("What would you like user? "))

    clear()
    return userInput

#function for checking userinput
def userInputYorNFunction(userInput):
    #checking the userInput
    userTester = ['y','n','Y','N']
    #if there input is not there than its traping them
    while userInput not in userTester:
        userInput = input("Please Enter (Y | N): ")
    userInput.lower()
    clear()
    return userInput



################---------------All The functions for the maze game------------------#############
#this is maing the maze with the value of width and hight

def findWidthAndHight():
    #setting the width\height before it is there
    userWidth = 0
    userHeight = 0
    #making sure its a number for width\hight
    print("\t\t--It can only be 1-20--\n\n")
    while userWidth <= 0 or userWidth >= 20:
        try:
            userWidth = int(input("How WIDE would you like your maze?: "))
        except:
            print("Please Enter a Number, grater than 0 and less then 20")
        if userWidth <= 0 or userWidth >= 20:
            print("\nNumber 1-20")
    clear()
    #height
    print("\t\t--It can only be 1-20--\n\n")
    while userHeight <= 0 or userHeight >= 20:
        try:
            userHeight = int(input("How Tall would you like your maze?: "))
        except:
            print("Please Enter a Number, grater than 0 and less then 20")
        if userHeight <= 0 or userHeight >= 20:
            print("\nNumber 1-20")
    clear()

    return userWidth, userHeight

def init_maze(width, height):
    #setting a new maze so its random every time
    maze = []
    display = []
    #What the posable thing could look like
    wallorHall = ["H", "W", "C", "X"]






    #this is for the range of the height make a new list 
    for i in range(0, height):
        line = []
        displayLine = []
        #than for the width set it in the range
        for j in range(0, width):
            line.append(wallorHall[random.randint(0,len(wallorHall) - 1)])
            #this is that the maze will look like
            displayLine.append(" ")
        display.append(displayLine)
        maze.append(line)



    return maze, display

#this is the function to call the maze games in the main code
def theWholeMazeGame():

    mazeGamePlay = input("\n\tDo you wish to enter?  ")
    mazeGamePlay = userInputYorNFunction(mazeGamePlay)

    #when asking for the width and height make sure to add 1 so the work
    #width = 20
    #height = 20

    width, height = findWidthAndHight()


    while mazeGamePlay.lower() == 'y':
        #setting vars that i want to have be reset after the game so the user can have a different playthought
        maze = []
        headingRowlist = []
        userXcord = 0
        userYcord = 0
        xcordOkay = []
        ycordOkay = []
        mazeCopy = []


        #the maze the play will use for this run
        maze, display = init_maze(width, height)
        mazeCopy = maze

        #this is setting values
        for i in range(0, width):
            headingRowlist.append(i + 1)
            xcordOkay.append(i + 1)

        for i in range(0, height):
            ycordOkay.append(i + 1)



        print("\n\t\t---Where would you like to start your adventure?---\n")

        time.sleep(1)

        print(f"X is --> {headingRowlist}")

        time.sleep(1)

        print("\nY is --V-Down-V--")

        time.sleep(1)


        display = mazeDisplay(display)
        userXcord = 0
        
        #GEtting the user starting X
        while userXcord not in xcordOkay:
            
            try:
                userXcord = int(input("\nX Location: "))
            except:
                print("\n----Please Enter a Number----")
            if userXcord not in xcordOkay:
                print(f"\nIT MUST BE BETWEEN 1 - {width}!!! ")

        #GEtting the user starting Y
        while userYcord not in ycordOkay:
            
            try:
                userYcord = int(input("\nY Location: "))
            except:
                print("\n----Please Enter a Number----")
            if userYcord not in ycordOkay:
                print(f"\nIT MUST BE BETWEEN 1 - {height}!!! ")

        userYcord -= 1
        userXcord -= 1

        clear()

        #setting the starting location for the user
        #display[userYcord][userXcord] = ('P')
        display[userYcord][userXcord] = "P"
        maze[userYcord][userXcord] = "P"
        
        #this is than showing them where they are starting
        display = mazeDisplay(display)

        #Asking where they would like to move to 
        canPlayerMove = "y"

        userYcordLocation = userYcord
        userXcordLocation = userXcord

        totalValue = width * height
        #input("Debug")
        #clear()
        #print(maze)
        #print("\n\n")
        #print(totalValue)
        #print(len(maze))


        totalWalls = 0
        totalChest = 0
        totalHall = 0
        totalMonster = 0
        totalPlayer = 0
        tallyTotal = totalValue
        totalItems = 0

        while tallyTotal != 0 :
                for i in range(0, len(maze)):
                #print(f"\nI: {i} Mazelen: {len(maze[i])}\n")
                    for j in range(0, len(maze[i])):
                    #print(f"J: {j} Maze item: {maze[i][j]}")
                        if maze[i][j] == "X":
                            totalMonster += 1
                            tallyTotal -= 1
                        elif maze[i][j] == "W":
                            totalWalls += 1
                            tallyTotal -= 1

                            totalValue -= 1
                        elif maze[i][j] == "C":
                            totalChest += 1
                            tallyTotal -= 1
                        elif maze[i][j] == "P":
                            totalPlayer += 1
                            tallyTotal -= 1
                            totalValue -= 1
                        else:
                            totalHall += 1
                            tallyTotal -= 1

        totalItems += totalHall
        totalItems += totalChest
        totalItems += totalMonster
        totalMoves = 0

        print(f"\n\n----Total Spaces Avabile: {totalValue}-----\n")
        input(f"---You lose if moves made >= Total Space---\n\n\t--Press Enter--")
        #time.sleep(4)

        while totalValue >= totalMoves:
            
            
            #print(totalValue)
            #input(totalItems)
            clear()
            #print(f"\n----Total Moves Made: {totalMoves}-----\n")
            #print(f"Monster: {totalMonster}")
            #print(f"wall: {totalWalls}")
            #print(f"hall: {totalHall}")
            #print(f"chest: {totalChest}")
            #print(f"PLayer: {totalPlayer}")
            #input("\nNew Way")
            #clear()
            display = mazeDisplay(display)
            maze, display, userYcordLocation, userXcordLocation, totalValue, totalMoves = mazePlayerMovement(maze, display, userYcordLocation, userXcordLocation, totalValue, totalMoves )
            display = mazeDisplay(display)


            #print(f"\n----3.Total value run: {totalValue}-----\n")
            #totalValue += 1

            
            #totalItems += 1

            #if totalValue == totalMoves:
                #print("\n---Last-Move---")
                #time.sleep(3)

            totalValue -= 1
            totalMoves += 1

            #if totalValue == totalMoves:
                #print("\n---Last-Move---")
                #time.sleep(3)
            #print(f"\n\n----Total Spaces Avabile: {totalValue}-----\n")
            if totalValue <= totalMoves:
                print("\n---That was your last move---")
                time.sleep(2)
            input(f"\n----Total Moves Made: {totalMoves}-----\n\n\n\t--Press Enter--")
            



            
            #print(f"\n----4.Total value run: {totalValue}-----")
        
        #print(f"Monster: {totalMonster}")
        #print(f"wall: {totalWalls}")
        #print(f"hall: {totalHall}")
        #print(f"chest: {totalChest}")
        #print(f"PLayer: {totalPlayer}")
            

            
        clear()
        maze = mazeDisplayFinal(mazeCopy)
        print("YouRan out of moves")
        input("\n\n\n\t\t###############__________Old WAy_____________############")
        clear()
        while canPlayerMove.lower() != "n":
            display = mazeDisplay(display)
            maze, display, userYcordLocation, userXcordLocation = mazePlayerMovement(maze, display, userYcordLocation, userXcordLocation )
            display = mazeDisplay(display)



            canPlayerMove = input("\nCan you explore more?: ")
            clear()
            canPlayerMove = userInputYorNFunction(canPlayerMove)



        #this would be more for the score now from the movemtn player

        input("Changed")
        #Now send to new function for maze 





        #the end of the project
        mazeGamePlay = input("\n\tDo you wish to enter again?  ")
        mazeGamePlay = userInputYorNFunction(mazeGamePlay)


#this is for displaying to the user where they are in the maze
def mazeDisplay(display):
    displayCopy = display
    

    print("\t----------Map-----------")
    for i in range(0, len(displayCopy)):
        print(f"{i + 1:2}:   {displayCopy[i]}")


    return displayCopy

def mazeDisplayFinal(maze):
    mazeCopy = maze
    

    print("\t----------Map-----------")
    for i in range(0, len(mazeCopy)):
        print(f"{i + 1:2}:   {mazeCopy[i]}")


    return mazeCopy
    
# the full testing function ----- with out score -----if the is space behinde a wall 
def testing(mazeChange,playerLocationY,playerLocationX,displayChange, playerMovement,totalValue, totalMoves):
    if mazeChange [playerLocationY][playerLocationX] == "W":

        input("\n------Wall------\n\n\t--Press Enter--")
        #nif the value is w,a,s,d, for wall it sets the player back to the right spot
        if playerMovement.upper() == "W":
            
            playerLocationY += 1
            #playerLocationX += 1
        elif playerMovement.upper() == "A":
            #playerLocationY += 1
            playerLocationX += 1
        elif playerMovement.upper() == "S":
            playerLocationY -= 1
            #playerLocationX += 1
        else:
            #playerLocationY -= 1
            playerLocationX -= 1
        #the total displays
        displayChange[playerLocationY][playerLocationX] = mazeChange[playerLocationY][playerLocationX]
        totalValue += 1

        #totalMoves -= 1


        displayChange [playerLocationY][playerLocationX] = "P"
        mazeChange [playerLocationY][playerLocationX] = "#"
    #it than moves to the c
    elif mazeChange [playerLocationY][playerLocationX] == "C":
        chestFinds()
        displayChange [playerLocationY][playerLocationX] = "P"
        mazeChange [playerLocationY][playerLocationX] = "#"
    #This is for the x
    elif mazeChange [playerLocationY][playerLocationX] == "X":
        monsterFinds()
        displayChange [playerLocationY][playerLocationX] = "P"
        mazeChange [playerLocationY][playerLocationX] = "#"
    #this what happends with p
    elif mazeChange [playerLocationY][playerLocationX] == "P":
        input("\n---Starting Point---\n\n\t--PressEnter--")
        displayChange [playerLocationY][playerLocationX] = "P"
        mazeChange [playerLocationY][playerLocationX] = "#"
        totalValue += 1
    #this is what happends at the hall
    else:
        input("\n---Hall---\n\n\t--Press Enter--")
        displayChange [playerLocationY][playerLocationX] = "P"
        mazeChange [playerLocationY][playerLocationX] = "#"

    return mazeChange,playerLocationY,playerLocationX,displayChange, totalValue, totalMoves

#this is for the player movement in the maze
def mazePlayerMovement(maze, display,playerLocationY, playerLocationX, totalValue, totalMoves ):
    #print(f"width {width}")
    #input(f"Height {height}")
    totalValue = totalValue
    mazeChange = maze
    displayChange = display
    playerMovementOkay = ["W","A","S","D"]
    playerMovement = " "


    #playerLocationX = userXcord
    #playerLocationY = userYcord
    #upANdown -= 1
    #leftANright -= 1
    #print(f"width after {upANdown}")
    #input(f"Height after {leftANright}")


    #this is just for the input to be right
    while playerMovement.upper() not in playerMovementOkay:
        playerMovement = str(input("\nWhere would you like to move?: "))
        if playerMovement.upper() not in playerMovementOkay:
            print("It must be W, A, S, D")
    
    #addending the the player starting location
    #displayChange[userYcord][userXcord] = "#"
    #mazeChange[userYcord][userXcord] = "#"
    #print(mazeChange)

    #This is where it is
    if playerMovement.upper() == "W":
        
        #displayChange[playerLocationY][playerLocationX] = "#"

        #print(f"PLayer y {playerLocationY}")
        #print(f"PLayer x {playerLocationX}")
        playerLocationY -= 1
        #print(f"A PLayer y {playerLocationY}")
        #print(f"A PLayer x {playerLocationX}")

        #ege of map works
        if playerLocationY < 0:
            input("\n---You are at the ege of the map---\n\n\t--Press Enter--")
            playerLocationY += 1
            totalValue += 1

            totalMoves -= 1
        else:

            #displayChange[playerLocationY][playerLocationX] = mazeChange[playerLocationY][playerLocationX]
            playerLocationY += 1
            displayChange[playerLocationY][playerLocationX] = "#"
            mazeChange[playerLocationY][playerLocationX] == "#"
            playerLocationY -= 1
            
            if mazeChange[playerLocationY][playerLocationX] == "#":
                input("\n---You have been here---\n\n\t--Press Enter--")
                displayChange [playerLocationY][playerLocationX] = "P"
                totalValue += 1


                totalMoves -= 1
            else:
                mazeChange,playerLocationY,playerLocationX,displayChange, totalValue, totalMoves = testing(mazeChange,playerLocationY,playerLocationX,displayChange, playerMovement, totalValue, totalMoves)
                #input("testing")
                
                #if mazeChange [playerLocationY][playerLocationX] == "W":
                    #print("WAll")
                    #displayChange[playerLocationY][playerLocationX] = mazeChange[playerLocationY][playerLocationX]
                    #playerLocationY += 1
                    #displayChange [playerLocationY][playerLocationX] = "P"
                    #mazeChange [playerLocationY][playerLocationX] = "#"

                #elif mazeChange [playerLocationY][playerLocationX] == "C":
                    #chestFinds()
                    #displayChange [playerLocationY][playerLocationX] = "P"
                    #mazeChange [playerLocationY][playerLocationX] = "#"

                #elif mazeChange [playerLocationY][playerLocationX] == "X":
                    #monsterFinds()
                    #displayChange [playerLocationY][playerLocationX] = "P"
                    #mazeChange [playerLocationY][playerLocationX] = "#"

                #elif mazeChange [playerLocationY][playerLocationX] == "P":
                    #print("You have been here")
                    #displayChange [playerLocationY][playerLocationX] = "P"
                    #mazeChange [playerLocationY][playerLocationX] = "#"
                #else:
                    #print("Hall")
                    #displayChange [playerLocationY][playerLocationX] = "P"
                    #mazeChange [playerLocationY][playerLocationX] = "#"
                


        #displayChange[playerLocationY][playerLocationX] = mazeChange[playerLocationY][playerLocationX]
    
    elif playerMovement.upper() == "A":

        #print(f"PLayer y {playerLocationY}")
        #print(f"PLayer x {playerLocationX}")
        playerLocationX -= 1
        #print(f"A PLayer y {playerLocationY}")
        #print(f"A PLayer x {playerLocationX}")
        #print("LEnght V ")
        #print(len(mazeChange[playerLocationY]))

        if playerLocationX < 0:
            input("\n---You are at the ege of the map---\n\n\t--Press Enter--")
            playerLocationX += 1
            totalValue += 1

            totalMoves -= 1
            
        else:
            #displayChange[playerLocationY][playerLocationX] = mazeChange[playerLocationY][playerLocationX]


            playerLocationX += 1
            displayChange[playerLocationY][playerLocationX] = "#"
            playerLocationX -= 1
            

            if mazeChange[playerLocationY][playerLocationX] == "#":
                input("\n---You have been here---\n\n\t--Press Enter--")
                displayChange[playerLocationY][playerLocationX] = "P"
                totalValue += 1
                totalMoves -= 1
            else:
                mazeChange,playerLocationY,playerLocationX,displayChange, totalValue, totalMoves = testing(mazeChange,playerLocationY,playerLocationX,displayChange, playerMovement, totalValue, totalMoves)
                
                #input("testing")


                #if mazeChange [playerLocationY][playerLocationX] == "W":
                #    print("WAll")
                ##    displayChange[playerLocationY][playerLocationX] = mazeChange[playerLocationY][playerLocationX]
                #    playerLocationX += 1


                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"



                #elif mazeChange [playerLocationY][playerLocationX] == "C":
                #    chestFinds()
                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"
                #elif mazeChange [playerLocationY][playerLocationX] == "X":
                #    monsterFinds()
                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"

                #elif mazeChange [playerLocationY][playerLocationX] == "P":
                #    print("You have been here")
                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"
                #else:
                #    print("Hall")
                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"


        #displayChange[playerLocationY][playerLocationX] = mazeChange[playerLocationY][playerLocationX]

        
        #Ending of A
    
    elif playerMovement.upper() == "S":


        #print(f"PLayer y {playerLocationY}")
        #print(f"PLayer x {playerLocationX}")
        playerLocationY += 1
        #print(f"A PLayer y {playerLocationY}")
        #print(f"A PLayer x {playerLocationX}")

        #print(len(mazeChange))

        if playerLocationY >= len(mazeChange):
            input("\n---Edge of the map---\n\n\t--Press Enter--")
            playerLocationY = (len(mazeChange) - 1)
            #print(playerLocationY)
            totalValue += 1
            totalMoves -= 1
        else:
            #displayChange[playerLocationY][playerLocationX] = mazeChange[playerLocationY][playerLocationX]

            playerLocationY -= 1
            displayChange[playerLocationY][playerLocationX] = "#"
            playerLocationY += 1
            
            if mazeChange[playerLocationY][playerLocationX] == "#":
                input("\n---You have been here---\n\n\t--Press Enter--")
                displayChange [playerLocationY][playerLocationX] = "P"
                totalValue += 1
                totalMoves -= 1
            else:

                
                mazeChange,playerLocationY,playerLocationX,displayChange, totalValue, totalMoves = testing(mazeChange,playerLocationY,playerLocationX,displayChange, playerMovement, totalValue, totalMoves)
                
                #input("testing")


                #if mazeChange [playerLocationY][playerLocationX] == "W":
                #    print("WAll")
                #    displayChange[playerLocationY][playerLocationX] = mazeChange[playerLocationY][playerLocationX]

                #    playerLocationY -= 1


                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"

                #elif mazeChange [playerLocationY][playerLocationX] == "C":
                #    chestFinds()
                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"
                    
                #elif mazeChange [playerLocationY][playerLocationX] == "X":
                #    monsterFinds()
                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"

                #elif mazeChange [playerLocationY][playerLocationX] == "P":
                #    print("You have been here")
                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"

                #else:
                #    print("Hall")
                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"
        
    else:

        #print(f"PLayer y {playerLocationY}")
        #print(f"PLayer x {playerLocationX}")
        playerLocationX += 1
        #print(f"A PLayer y {playerLocationY}")
        #print(f"A PLayer x {playerLocationX}")

        #print(len(mazeChange[0]))

        #Just checking if the user has the 
        if playerLocationX >= len(mazeChange[0]):
            input("\n--You are at the ege of the map--\n\n\t--Press Enter--")
            playerLocationX -= 1
            totalValue += 1
            totalMoves -= 1
            
        else:
            

            #this is setting the location the player is comming from to a key
            playerLocationX -= 1
            displayChange[playerLocationY][playerLocationX] = "#"
            playerLocationX += 1
            

            #finding what the player is going to and doing what it is also seeting the way they go
            if mazeChange[playerLocationY][playerLocationX] == "#":
                input("\n---You have been here---\n\n\t--Press Enter--")
                totalValue += 1
                totalMoves -= 1
                displayChange[playerLocationY][playerLocationX] = "P"
            else:
                mazeChange,playerLocationY,playerLocationX,displayChange, totalValue,totalMoves = testing(mazeChange,playerLocationY,playerLocationX,displayChange, playerMovement, totalValue, totalMoves)
                
                
                #input("testing")


                #if mazeChange [playerLocationY][playerLocationX] == "W":
                #    print("WAll")

                #    displayChange[playerLocationY][playerLocationX] = mazeChange[playerLocationY][playerLocationX]



                #    playerLocationX -= 1

                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"


                #    totalValue += 1
                #elif mazeChange [playerLocationY][playerLocationX] == "C":
                #    chestFinds()
                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"
                #elif mazeChange [playerLocationY][playerLocationX] == "X":
                #    monsterFinds()
                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"

                #elif mazeChange [playerLocationY][playerLocationX] == "P":
                #    print("You have been here")
                #    totalValue += 1
                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"
                #else:
                #    print("Hall")
                #    displayChange [playerLocationY][playerLocationX] = "P"
                #    mazeChange [playerLocationY][playerLocationX] = "#"
        #end of the "D"movement


    
    #input("")
    clear()


    return mazeChange, displayChange, playerLocationY, playerLocationX, totalValue , totalMoves


def chestFinds():
    print("Chest")
    hAHALuck = random.randint(0,1000000)
    print(hAHALuck)


    input()
    


def monsterFinds():
    print("Monster")
    hAHALuck = random.randint(0,1000000)
    print(hAHALuck)


    input()


##############--------------Main Code-------------#################

#WElcoming the user
print("\t\t----Welcome to the maze-----")


#time.sleep(2)


#getting user input that checking keeping this
#mazeGamePlay = input("\n\tDo you wish to enter?  ")



#this will run IF the player does say yes in not than it will skip
#This will need to be an input for later,
#width = 5
#height = 5

userMenuChoise = menu()

#main game loop
while userMenuChoise != 4:

    if userMenuChoise == 1:

        #THis might need to return score, userName, width, hight, or a list of it
        theWholeMazeGame()




    elif userMenuChoise == 2:
        print("\t2\n")
    elif userMenuChoise == 3:
        print("\t3\n")
    else:
        print("\t4\n")
    
    userMenuChoise = menu()




print("\n\n\t\t----I hope you liked my project----")

input("\n\t\t------Press 'Enter' to leave-------")