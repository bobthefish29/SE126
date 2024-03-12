#David Punchak





#The program has gone thought a lot of changes in the time i have worked on it, I wanted it to be like a maze that has a start than the player goes around that maze and along the way they get prizes
#the way it is not the player moves around a dark room and if they find a chest they get points if they find a monster they lose points. 
#The game ends when the user runs out of moves, than they get a totally intential extra move after they go thought the whole maze. 


#the display does look like a list but it was not able to have the turtule program to have the display at the end.
#


#Just need to add coments, 

#tmr do some live testing on mom and dad, fix up the prints and stuff and the slide show for class. 




##################-------------Imports------------############
import random
import csv
import time
from os import system, name 


###########----------------Setting global Vars / lists----------------##################
userMenuChoise = 0

score = []
userName = []
width  = []
height = []

totalList = []

####################------------------Adding the values to the list-----------------#####################

#this is just importing a random value
with open("FinalProject/TextFiles/Maze.csv") as csvFile:
    file = csv.reader(csvFile)
    for rec in file:
        
        score.append(rec[0])
        userName.append(rec[1])
        width.append(rec[2])
        height.append(rec[3])
    
        totalList.append([int(rec[0]),rec[1],int(rec[2]),int(rec[3])])





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
    userOkay = [1,2,3,4]
    UserInputtest = -1
    print("What would you like to do user")
    print("1. Play maze")
    print("2. Veiw score board")
    print("3. View map layout.")
    print("4. Leave")


    while UserInputtest not in userOkay:
        try:
            UserInputtest = int(input("\nWhat would you like user? "))
        except:
            print("\n----Please enter a number-----")
        if UserInputtest not in userOkay:
            print("\n--Make user its (1,2,3,4)")
        


        

    clear()
    return UserInputtest

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

#this is just making the maze
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

#this is the function to call the maze games in the main code, its just so i dont have to have a huge main code and its just in a function
def theWholeMazeGame(totalList):
    copyList = totalList
    mazeGamePlay = input("\n\tDo you wish to enter?  ")
    mazeGamePlay = userInputYorNFunction(mazeGamePlay)

    #when asking for the width and height make sure to add 1 so the work
    #width = 20
    #height = 20

    width, height = findWidthAndHight()


    while mazeGamePlay.lower() == 'y':
        #setting vars that i want to have be reset after the game so the user can have a different playthought
        score = 0
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
        #canPlayerMove = "y"

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
        totalMoveCount = 0

        print(f"\n\n----You have a total of: {totalValue} moves-----\n")
        #print({totalValue - totalMoves})
        input(f"---You lose when you run out of moves---\n\n\t--Press Enter--")
        #time.sleep(4)

        while totalValue >= totalMoves:
            
            
            #print(totalValue)
            #input("Before run \n\n")


            clear()
            #print(f"\n----Total Moves Made: {totalMoves}-----\n")
            #print(f"Monster: {totalMonster}")
            #print(f"wall: {totalWalls}")
            #print(f"hall: {totalHall}")
            #print(f"chest: {totalChest}")
            #print(f"PLayer: {totalPlayer}")
            #input("\nNew Way")
            #clear()


            #print(f"\tDebug:\nTotal moves: {totalMoves}\nMovesLeft: {totalValue - totalMoves}\nTotal Value: {totalValue}")
            #input(f"Before movement")

            display = mazeDisplay(display)
            maze, display, userYcordLocation, userXcordLocation, totalValue, totalMoves, score = mazePlayerMovement(maze, display, userYcordLocation, userXcordLocation, totalValue, totalMoves, score )
            display = mazeDisplay(display)


            #print(f"\tDebug:\nTotal moves: {totalMoves}\nMovesLeft: {totalValue - totalMoves}\nTotal Value: {totalValue}")
            #input(f"after movement")



            #print(f"\n----3.Total value run: {totalValue}-----\n")
            #totalValue += 1

            
            #totalItems += 1

            #print(f"before if ")
            #print(f"\n\n\tDebug:\n\nTotalmoves: {totalMoves}")

            if totalMoves < 0:
                totalMoves = 0
                totalMoveCount += 1

                #print("\n---Last-Move---")
                #time.sleep(3)
            else:
                totalMoves += 1
                totalMoveCount += 1

            #print(f"after if ")
            #print(f"\n\n\tDebug:\n\nTotalmoves: {totalMoves}")
            
            #testing1 = totalMoves - totalValue
            #testing2 = totalValue - totalMoves

            #print(f"before adding +1 to total and -1 from move and after if ")
            #print(f"\n\n\tDebug:\n\nTotalmoves: {totalMoves}\nMovesLeft: {totalValue - totalMoves}\nTotal Value: {totalValue}\n\nTesting1: {testing1}\ntesting2: {testing2}")
            

            #totalMoves += 1
            totalValue -= 1

            #totalMoves += 1

            #testing1 = totalMoves - totalValue
            #testing2 = totalValue - totalMoves
            #testing2 += 1
            #print(f"after adding +1 to total and -1 from move")
            #print(f"\n\n\tDebug:\nTotal moves: {totalMoves}\nMovesLeft: {totalValue - totalMoves}\nTotal Value: {totalValue}\n\nTesting: {testing1}\Testing2 += 1: {testing2}")
            
            
            
            #if totalValue == totalMoves:
                #print("\n---Last-Move---")
                #time.sleep(3)
            #print(f"\n\n----Total Spaces Avabile: {totalValue}-----\n")
            #if totalValue <= totalMoves:
                
                #input("testing")
                #if lastmovecount == 1:
                    #input("\n---This is your last move---\n\n\t---Press Enter---")
                #else:
                    #input("\n--You ran out of moves--\n\n\t---Press Enter---")
                #lastmovecount += 1
            #else:
                #print(f"\n\n----Total Spaces Avabile: {totalValue}-----\n")
            
            if (totalValue - totalMoves) <= 0:
                if (totalValue - totalMoves) == -1:
                    input("----------------goodJob-----------------")
                else:
                    input("\n\n\t\t-----------Bonus Move-------------------------------")
                
            else:
                input(f"\nMoves Left: {totalValue - totalMoves}-----\n\n\n\t--Press Enter--")
                #input(f"\n----Total Moves Made: {totalMoveCount}-----\n\n\n\t--Press Enter--")
                #time.sleep(2)
            
                #print("\n---Was last move----")
            #print(f"\n\n----Total Spaces Avabile: {totalValue}-----\n")
            #print(f"Moves Left {totalValue - totalMoves}")
            #input(f"\n----Total Moves Made: {totalMoves}-----\n\n\n\t--Press Enter--")
            



            
            #print(f"\n----4.Total value run: {totalValue}-----")
        
        #print(f"Monster: {totalMonster}")
        #print(f"wall: {totalWalls}")
        #print(f"hall: {totalHall}")
        #print(f"chest: {totalChest}")
        #print(f"PLayer: {totalPlayer}")
            

            
        clear()
        maze = mazeDisplayFinal(mazeCopy)

        #print("\n---You ran out of moves--")
        #input("\n\n\n\t\t###############__________Old WAy_____________############")
        #clear()
        #while canPlayerMove.lower() != "n":
            #display = mazeDisplay(display)
            #maze, display, userYcordLocation, userXcordLocation = mazePlayerMovement(maze, display, userYcordLocation, userXcordLocation )
            #display = mazeDisplay(display)



            #canPlayerMove = input("\nCan you explore more?: ")
            #clear()
            #canPlayerMove = userInputYorNFunction(canPlayerMove)



        #this would be more for the score now from the movemtn player

        #input("Changed")
        #Now send to new function for maze 





        #the end of the project
        print(f"\nScore: {score}")
        mazeGamePlay = input("\n\tDont like your score?\n\tWish to enter again(Y/N)?:  ")
        mazeGamePlay = userInputYorNFunction(mazeGamePlay)


    clear()

    print("\n----Well done user----\n")
    print(f"\nYou got a score of {score}")

    userName = input("\nWhat should we call you?: ")



    copyList.append([score,userName, width, height])
    clear()

    
    return copyList


#this is for displaying to the user where they are in the maze
def mazeDisplay(display):
    displayCopy = display
    

    print("\t----------Map-----------")
    for i in range(0, len(displayCopy)):
        print(f"{i + 1:2}:   {displayCopy[i]}")


    return displayCopy

#This is just a display for the end where it shows the orginal list to the user
def mazeDisplayFinal(maze):
    mazeCopy = maze
    

    print("\t----------Map-----------")
    for i in range(0, len(mazeCopy)):
        print(f"{i + 1:2}:   {mazeCopy[i]}")


    return mazeCopy
    
# the full functon for what the player might run into
def testing(mazeChange,playerLocationY,playerLocationX,displayChange, playerMovement,totalValue, totalMoves, score):
    if mazeChange [playerLocationY][playerLocationX] == "W":

        input("\n------Wall------\n\n\t--Press Enter--")
        #nif the value is w,a,s,d, for wall it sets the player back to the right spot
        if playerMovement.upper() == "W":
            displayChange [playerLocationY][playerLocationX] = "W"
            playerLocationY += 1
            #playerLocationX += 1
        elif playerMovement.upper() == "A":
            #playerLocationY += 1
            displayChange [playerLocationY][playerLocationX] = "W"
            playerLocationX += 1
        elif playerMovement.upper() == "S":
            displayChange [playerLocationY][playerLocationX] = "W"
            playerLocationY -= 1
            #playerLocationX += 1
        else:
            #playerLocationY -= 1
            displayChange [playerLocationY][playerLocationX] = "W"
            playerLocationX -= 1
        #the total displays
        
        #displayChange[playerLocationY][playerLocationX] = "W"
        #mazeChange[playerLocationY][playerLocationX] = "W"
        #displayChange [playerLocationY][playerLocationX] = "#"
        #mazeChange[playerLocationY][playerLocationX] = displayChange[playerLocationY][playerLocationX]


        #totalMoves -= 1
        #input(displayChange[playerLocationY][playerLocationX])
        #input(mazeChange[playerLocationY][playerLocationX])
        #input(displayChange)
        #input(mazeChange)

        #works
        displayChange[playerLocationY][playerLocationX] = mazeChange[playerLocationY][playerLocationX]
        displayChange [playerLocationY][playerLocationX] = "P"
        mazeChange [playerLocationY][playerLocationX] = "#"
        totalValue += 1

    #it than moves to the c
    elif mazeChange [playerLocationY][playerLocationX] == "C":
        score = chestFinds(score)
        displayChange [playerLocationY][playerLocationX] = "P"
        mazeChange [playerLocationY][playerLocationX] = "#"

        totalMoves -= 1
    #This is for the x
    elif mazeChange [playerLocationY][playerLocationX] == "X":
        score = monsterFinds(score)
        displayChange [playerLocationY][playerLocationX] = "P"
        mazeChange [playerLocationY][playerLocationX] = "#"
        totalMoves -= 1
    #this what happends with p
    elif mazeChange [playerLocationY][playerLocationX] == "P":
        input("\n---Starting Point---\n\n\t--PressEnter--")
        displayChange [playerLocationY][playerLocationX] = "P"
        mazeChange [playerLocationY][playerLocationX] = "#"
        
        totalMoves -= 1
        totalMoves -= 1
        #totalValue += 1
    #this is what happends at the hall
    else:
        input("\n---Hall---\n\n\t--Press Enter--")
        displayChange [playerLocationY][playerLocationX] = "P"
        mazeChange [playerLocationY][playerLocationX] = "#"
        totalMoves -= 1
        

    return mazeChange,playerLocationY,playerLocationX,displayChange, totalValue, totalMoves, score

#this is for the player movement in the maze, this is if they move w,a,s,d.
def mazePlayerMovement(maze, display,playerLocationY, playerLocationX, totalValue, totalMoves, score ):
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
                mazeChange,playerLocationY,playerLocationX,displayChange, totalValue, totalMoves,score = testing(mazeChange,playerLocationY,playerLocationX,displayChange, playerMovement, totalValue, totalMoves, score)
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
                mazeChange,playerLocationY,playerLocationX,displayChange, totalValue, totalMoves, score = testing(mazeChange,playerLocationY,playerLocationX,displayChange, playerMovement, totalValue, totalMoves, score)
                
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

                
                mazeChange,playerLocationY,playerLocationX,displayChange, totalValue, totalMoves, score = testing(mazeChange,playerLocationY,playerLocationX,displayChange, playerMovement, totalValue, totalMoves, score)
                
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
                mazeChange,playerLocationY,playerLocationX,displayChange, totalValue,totalMoves, score = testing(mazeChange,playerLocationY,playerLocationX,displayChange, playerMovement, totalValue, totalMoves, score)
                
                
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


    return mazeChange, displayChange, playerLocationY, playerLocationX, totalValue , totalMoves, score

#this is what will happen if the user finds a chest
def chestFinds(score):
    print("\nYou found a chest :)")
    hAHALuck = random.randint(6000,10000)
    print(f"\nYou have ganed {hAHALuck} points\n ")

    score += hAHALuck

    if score >= 10000000000:
        print("Wow you are at the score cap\n")
        score = 10000000000
    else:
        print(f"Your Score is {score}\n")

    input(f"\n\n\t-----Please Press Enter-----")
    return score

#this is what will hapen if the user Finds a monster
def monsterFinds(score):
    print("\nYou found a monster :(")
    hAHALuck = random.randint(5000,10000)
    print(f"\nYou lost {hAHALuck} points\n")

    score -= hAHALuck

    if score <= -1:
        print("You just lost all your point\n")
        score = 0
    else:
        print(f"Your Score is {score}\n")

    input(f"\n\n\t-----Please Press Enter-----")
    return score



################--------Function's for the leaderboard-----------##############

#This is more of a sorting for the leaderboard, its more of a print function. 
def leaderBoardScore(totalList):

    scoreTestingList = totalList

    #print(scoreTestingList)

    for i in range(0, len(scoreTestingList) - 1):#outter loop

        #print("OUTER LOOP! i = ", i)

        #this is the loop for moving the number to the right place, 
        for index in range(0, len(scoreTestingList) - 1):#inner loop

            #print("\t INNER LOOP! k = ", index)

            
            if (scoreTestingList[index] < scoreTestingList[index + 1]):

                #print("\t\t SWAP! ", scoreTestingList[index][0], "<-->", scoreTestingList[index + 1][0])

                #swaping score
                temp = scoreTestingList[index][0]
                scoreTestingList[index][0] = scoreTestingList[index + 1][0]
                scoreTestingList[index + 1][0] = temp

                #swaping userName
                temp = scoreTestingList[index][1]
                scoreTestingList[index][1] = scoreTestingList[index + 1][1]
                scoreTestingList[index + 1][1] = temp

                #swaping width
                temp = scoreTestingList[index][2]
                scoreTestingList[index][2] = scoreTestingList[index + 1][2]
                scoreTestingList[index + 1][2] = temp
                
                #swaping hight
                temp = scoreTestingList[index][3]
                scoreTestingList[index][3] = scoreTestingList[index + 1][3]
                scoreTestingList[index + 1][3] = temp



    #print(f"\n{scoreTestingList}")

    #input("Testing")
    #this list is sorted by score, it will be more used for the display not the searches
    return scoreTestingList



def learderBoardUserName(totalList):
    userNameList = totalList
    
    #the loop for sorting the values into the name value orfer for the search
    for i in range(0, len(userNameList) - 1):#outter loop

        #print("OUTER LOOP! i = ", i)

        #this is the loop for moving the number to the right place, 
        for index in range(0, len(userNameList) - 1):#inner loop

            #print("\t INNER LOOP! k = ", index)

            
            if (userNameList[index][1].upper() > userNameList[index + 1][1].upper()):

                #print("\t\t SWAP! ", scoreTestingList[index][0], "<-->", scoreTestingList[index + 1][0])

                #swaping score
                temp = userNameList[index][0]
                userNameList[index][0] = userNameList[index + 1][0]
                userNameList[index + 1][0] = temp

                #swaping userName
                temp = userNameList[index][1]
                userNameList[index][1] = userNameList[index + 1][1]
                userNameList[index + 1][1] = temp

                #swaping width
                temp = userNameList[index][2]
                userNameList[index][2] = userNameList[index + 1][2]
                userNameList[index + 1][2] = temp
                
                #swaping hight
                temp = userNameList[index][3]
                userNameList[index][3] = userNameList[index + 1][3]
                userNameList[index + 1][3] = temp
    #input("3\n")
    #print(userNameList)
    #input("4\n")

    search = input("\nWhat 'UserName' are you looking for?: ")

    #the lowest index in that list and the lowest point
    min = 0
    #the max number of 
    max = len(userNameList) - 1       #can also use len(listName) for 'records' value

    #this is the midpoint to see if its on one half or the other
    mid = int((min + max) / 2)
    
    #the main loop for finding it
    while (min < max and search.upper() != userNameList[mid][1].upper()):
        #This is for if the search is the 
        #print(userNameList[mid][1].upper())
        #input("")
        if search.upper() < userNameList[mid][1].upper():

            max = mid - 1

        else:

            min = mid + 1

        mid = int((min + max) / 2)

        #if mid == 8:
            #print("8")
        #else:
            #print(mid)
    #input("\nAfter")
    #print(userNameList[mid][1].upper())
        
    #if they find it, if not
    if search.upper() == userNameList[mid][1].upper():
        #userNameList = leaderBoardScore(userNameList)
        
        print(f"\n{search:15}\tScore: {userNameList[mid][0]}\t Width: {userNameList[mid][2]}\t Height: {userNameList[mid][3]}")
        input("\n\n\t------Press Enter-------")
        #found them! use 'mid' for index of found search item

    else:

        #boooo not found
        #print("\n-----UserName\tScore\tWidth\thight-----------")
        print(f"\nThere is no userName called '{search}', You could have entered it wrong :(")
        input("\n\n\t------Press Enter-------")
        





    #returning he list
    
    return userNameList


def leaderboardMenu():
    userOkay = [1,2]
    userInput = -1
    print("\nWhat would you like to do user\n")
    print("1. Look for user Name")
    print("2. Leave")


    while userInput not in userOkay:
        try:
            userInput = int(input("\nWhat would you like user? "))
        except:
            print("\n---Please Enter a number---")
        if userInput not in userOkay:
            print("\n--1 or 2--")



    #clear()
    return userInput



def leaderBoardFunction(totalList):
    testingList = totalList
    
    totalList = leaderBoardScore(totalList)
    print("\n\n\t-----Leader Board-----\n")
    print(f"{'Rank':4}    {'Score':10}   {'UserName':20}   {'Width':5}       {'Height'}")
    print("--------------------------------------------------------------------")
    for i in range(0,10):
        print(f"{i + 1:4}: {testingList[i][0]:10} | {testingList[i][1]:20} |  {testingList[i][2]:5}   |    {testingList[i][3]}")

    userInput = leaderboardMenu()

    
    while userInput != 2:
        totalList = leaderBoardScore(totalList)
        clear()
        print("\n\n\t-----Leader Board-----\n")
        print(f"{'Rank':4}    {'Score':10}   {'UserName':20}   {'Width':5}       {'Height'}")
        print("--------------------------------------------------------------------")
        for i in range(0,10):
            print(f"{i + 1:4}: {testingList[i][0]:10} | {testingList[i][1]:20} |  {testingList[i][2]:5}   |    {testingList[i][3]}")


    
        testingList = learderBoardUserName(testingList)

        userInput = leaderboardMenu()
    

    #print(totalList[0][1])



################----------Functions for the last option the display----------------################
        
def option3Display(maze):
    mazeCopy = maze
    

    print("\t----------Map-----------")


    for i in range(0, len(mazeCopy[0])):
        print(f"{i + 1:2}:   {mazeCopy[i]}")


    print("\nThis is what a map could look like")

    input("\n\n\t---Press Enter---")
    return mazeCopy

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

        totalList = theWholeMazeGame(totalList)
        clear()
    elif userMenuChoise == 2:
        leaderBoardFunction(totalList)
        clear()
    elif userMenuChoise == 3:
        width, height = findWidthAndHight()
        maze,trash = init_maze(width, height)
        trash = []
        option3Display(maze)
        clear()
    else:
        print("This code will never be seen :)")
    
    userMenuChoise = menu()




print("\n\n\t\t----I hope you liked my project----")

input("\n\t\t------Press 'Enter' to leave-------")