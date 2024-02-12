#david punchak
#january 30 - feb 
#MidTerm Project
#SE126.10


#Menu than based on the user pick it gives them the type of game for it. 

#have the menu than the user picks 1-3 

#1: long & lat game
#2: 
#3: exit

#making a long and lat project 
#giving a location that would be given a random 4 and the user has to guess. 
#

#------------Example----------
#What is the location of hover dam

#long lat 1
#long lat 2
#long lat 3
#long lat 4

#what do you think it is: 

#wrong - take one life away, move to next long and lat
#correct - Add one point, move to next long and lat.

#------------------The location for the importing of other recorces---------------

#Getting the imports for the other stuff that i am using
import random
import csv
import time
from os import system, name 

#----------------------This is where i am making the lists and the vars------------------------------------
#the lists for the long and lat game
location = []
long = []
lat = []
longLat2d = []

ranlonglat = random.randint(0, 41)

#the lists for the pokemon game
pokeNum = []
pokeName = []
pokeType = []
pokeType2 = []
pokeTotal = []
pokeAtt = []
pokeDef = []
pokeAttSpeed = []
pokeDefSpeed = []
pokeSpeed = []
pokeGen = []
pokeLeg = []
pokeAll =[]

playerPokemon = []

#the vars for the projects
randDeside = 0
coins = 0


#--------------------This is where i am going to be adding the values to there respected list before i use them.

#this is for the loop for long and lat game
with open("MidTermProject/TextFile/locations.txt", encoding = "utf-8") as longLatFile:#encodeing was from kt and conner?

    file = csv.reader(longLatFile)

    for rec in file:
        location.append(rec[0])
        long.append(float(rec[1]))
        lat.append(float(rec[2]))
    #making the 2d list 
    
    for i in range (0, len(location)):
        longLat2d.append([location[i],long[i],lat[i]])
    #print(longLat2d)
#out of loop

#this is the loop for the pokemon game
with open("MidTermProject/TextFile/Pokemon.csv") as pokeFile:

    pokiefile = csv.reader(pokeFile)

    for rec in pokiefile:
        #adding the rec of the pokemon list to there location
        pokeNum.append(int(rec[0]))
        
        pokeName.append(rec[1])
        
        pokeType.append(rec[2])
        
        #This is there so if the pokemon has a type 2 or not
        if rec[3] == "":
            pokeType2.append("NUN")
        else:
            pokeType2.append(str(rec[3]))
        
        
        #readding the values to there lists
        pokeTotal.append(int(rec[4]))
        pokeAtt.append(int(rec[5]))
        pokeDef.append(int(rec[6]))
        pokeAttSpeed.append(int(rec[7]))
        pokeDefSpeed.append(int(rec[8]))
        pokeSpeed.append(int(rec[9]))

        pokeGen.append(int(rec[11]))

        #print(str(rec[12]))
        if str(rec[12]) == "False":
            pokeLeg.append("No")
        else:
            pokeLeg.append("Yes")
    #making the 2d list for the pokiemon
    for i in range(0, len(pokeNum)):
        pokeAll.append([pokeNum[i], pokeName[i], pokeType[i], pokeType2[i], pokeTotal[i], pokeAtt[i], pokeDef[i], pokeAttSpeed[i], pokeDefSpeed[i], pokeSpeed[i], pokeGen[i], pokeLeg[i]])
    

#----------------------------------Functions------------------------------
#this is where the functions are going ton be for my program
#It will be most of my program will be in the functions than it will have so stuff out of the functions

#This is the clear function, it clears the terminal so it makes it look better
def clear():

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

#menu function
def menu():
    #Printing the menu
    print("\n1. Play the hard Long and Lat game. :)")
    print("2. Get a random pokemon ?")
    print("3. See Pokemon (basic)")
    print("4. Quit my project :(")
    #getting the input
    userInput= input("\nWhat would you like to do user(1-4)?: ")

    #print(userInput)

    #The loop to trap the user in, than sending it out as a string that i need to cast as a int when i call it.
    while userInput != "1" and userInput != "2" and userInput != "3" and userInput != "4":
        print("Wrong")
        userInput= input("\nWhat would you like to do user(1-4)?: ")

    time.sleep(2)
    clear()
    return userInput

#this is the function to call the long and lat game
def longLatGame(money):

    #The starting for the game


    #printing for the user to read
    print("------This game is hard------\n")
    print(f"\tYou have {money} coins")
    gamePicker = input("\nGame 1 more money, more Qustions\nGame 2 less money, less qustions\n\n(1 or 2): ")
    while gamePicker != "1" and gamePicker != "2":
        print("wrong")
        gamePicker = input("\nGame 1 more money, more Qustions\nGame 2 less money, less qustions\n\n(1 or 2): ")

    
    print("\n------Good luck------")



    #THis is the sleep function, it pauses the terminal than the clear function clears the terminal
    time.sleep(3)
    clear()
    
    #having the local vars for the function

    
        
    if gamePicker == "1":
        money = moreRoundMoreMoney(money)
    else:
        money = lessRoundLessMoney(money)
            
        
    #print("out of loop ")
    #print(f"Round count {roundCount}")
    print(f"You were able to get ${money} this time")
    time.sleep(2)


    return money

#-------------Sub long lat functions---------------
#Sub function for the long lat game that would give more money and have more rounds
def moreRoundMoreMoney(money):
    runTime = 10
    gameList = []
    copyList = []
    money = money
    

    while runTime != 0: 
        print(f"\t--{runTime} more qustion('s)--\n")
        copyList = longLat2d
        #copyList = longLat2d
        #copyList.append(longLat2d)

        #print(f"CopyList {copyList}")
            
        #gameList = []
        rand_num = 0
        start_len = len(longLat2d)
        index = 0
        #print(f"Start len: {start_len}")
        #print(index)
        while index < start_len:
            #THis is sorting the list to make it into a random list
            #print(f"\n------1Run time: {index}------------")
            #print(f"1Copy len:{len(copyList)}")
            #Setting to a random num based on copy
            rand_num = random.randint(0, len(copyList))
            #print(f"1Rand num: {rand_num}")
            #if its over than it would subtract than set it to that, the -1 is because the it index would set it to 0 instead
            if rand_num == -1:
                rand_num = 0
            elif rand_num >= len(copyList):
                rand_num -= 1
                #print("\t------over-------")

            gameList.append(copyList[rand_num])

            index += 1


        randomPlace = random.randint(0, len(gameList))
        randomPlace1 = random.randint(0, len(gameList))
        randomPlace2 = random.randint(0, len(gameList))
        randomPlace3 = random.randint(0, len(gameList))
    
        #this is for if the random number is equal or grader than the len of the list it wont brake and say its out of range
        if randomPlace == -1:
            randomPlace = 0
        elif randomPlace >= len(gameList):
            randomPlace -= 1
        if randomPlace1 == -1:
            randomPlace1 = 0
        elif randomPlace1 >= len(gameList):
            randomPlace1 -= 1
        if randomPlace2 == -1:
            randomPlace2 = 0
        elif randomPlace2 >= len(gameList):
            randomPlace2 -= 1
        if randomPlace3 == -1:
            randomPlace3 = 0
        elif randomPlace3 >= len(gameList):
            randomPlace3 -= 1




        print(f"What is the location of {gameList[randomPlace][0]}")

        #Will alwasy be the same answer of a to get coins
        print(f"\nA. Lat: {float(gameList[randomPlace][1]):.2f} Long: {float(gameList[randomPlace][2]):.2f}")

        print(f"B. Lat: {float(gameList[randomPlace1][1]):.2f} Long: {float(gameList[randomPlace1][2]):.2f}")
        print(f"C. Lat: {float(gameList[randomPlace2][1]):.2f} Long: {float(gameList[randomPlace2][2]):.2f}")
        print(f"D. Lat: {float(gameList[randomPlace3][1]):.2f} Long: {float(gameList[randomPlace3][2]):.2f}")


        

        longLatGamePick = input("\nWhat is your answer: ")

        while longLatGamePick != "A" and longLatGamePick != "a" and longLatGamePick != "B" and longLatGamePick != "b" and longLatGamePick != "C" and longLatGamePick != "c" and longLatGamePick != "D" and longLatGamePick != "d":
            print("-------You Have to pick A,B,C,D silly---------")
            longLatGamePick = input("\nWhat is your answer: ")


        for i in range(0, len(location)):
            gameList.pop(0)

        #print(f"After gamelist : {gameList}")
        index = 0
        copyList = []
        
        #if #the long, lat the user picks == the rec location in the list: true

        #this is where i am stuck, 
        if longLatGamePick == "A" or longLatGamePick == "a":
            money += 1
        elif longLatGamePick == "B" or longLatGamePick == "b":
            money += 0
        elif longLatGamePick == "C" or longLatGamePick == "c":
            money += 0
        else:
            money += 0



        runTime -= 1
        #print(runTime)
        
        clear()

    return money

#Sub function for the long, lat game aboue less money less rounds
def lessRoundLessMoney(money):
    runTime = 5
    gameList = []
    copyList = []
    money = money
    

    #print(f"runTime: {runTime}")
    #copyList = []

    while runTime != 0:  
        print(f"\t--{runTime} more qustion('s)--\n")
        copyList = longLat2d
        #copyList = longLat2d
        #copyList.append(longLat2d)

        #print(f"CopyList {copyList}")
            
        #gameList = []
        rand_num = 0
        start_len = len(longLat2d)
        index = 0
        #print(f"Start len: {start_len}")
        #print(index)
        while index < start_len:
            #THis is sorting the list to make it into a random list
            #print(f"\n------1Run time: {index}------------")
            #print(f"1Copy len:{len(copyList)}")
            #Setting to a random num based on copy
            rand_num = random.randint(0, len(copyList))
            #print(f"1Rand num: {rand_num}")
            #if its over than it would subtract than set it to that, the -1 is because the it index would set it to 0 instead
            if rand_num == -1:
                rand_num = 0
            elif rand_num >= len(copyList):
                rand_num -= 1
                #print("\t------over-------")

            gameList.append(copyList[rand_num])

            index += 1


        randomPlace = random.randint(0, len(gameList))
        randomPlace1 = random.randint(0, len(gameList))
        randomPlace2 = random.randint(0, len(gameList))
        randomPlace3 = random.randint(0, len(gameList))
    
        #this is for if the random number is equal or grader than the len of the list it wont brake and say its out of range
        if randomPlace == -1:
            randomPlace = 0
        elif randomPlace >= len(gameList):
            randomPlace -= 1
        if randomPlace1 == -1:
            randomPlace1 = 0
        elif randomPlace1 >= len(gameList):
            randomPlace1 -= 1
        if randomPlace2 == -1:
            randomPlace2 = 0
        elif randomPlace2 >= len(gameList):
            randomPlace2 -= 1
        if randomPlace3 == -1:
            randomPlace3 = 0
        elif randomPlace3 >= len(gameList):
            randomPlace3 -= 1




        print(f"What is the location of {gameList[randomPlace][0]}")


        print(f"\nA. Lat: {float(gameList[randomPlace][1]):.2f} Long: {float(gameList[randomPlace][2]):.2f}")

        print(f"B. Lat: {float(gameList[randomPlace1][1]):.2f} Long: {float(gameList[randomPlace1][2]):.2f}")
        print(f"C. Lat: {float(gameList[randomPlace2][1]):.2f} Long: {float(gameList[randomPlace2][2]):.2f}")
        print(f"D. Lat: {float(gameList[randomPlace3][1]):.2f} Long: {float(gameList[randomPlace3][2]):.2f}")



        longLatGamePick = input("\nWhat is your answer: ")

        while longLatGamePick != "A" and longLatGamePick != "a" and longLatGamePick != "B" and longLatGamePick != "b" and longLatGamePick != "C" and longLatGamePick != "c" and longLatGamePick != "D" and longLatGamePick != "d":
            print("-------You Have to pick A,B,C,D silly---------")
            longLatGamePick = input("\nWhat is your answer: ")


        for i in range(0, len(location)):
            gameList.pop(0)

        #print(f"After gamelist : {gameList}")
        index = 0
        copyList = []
        
        #if #the long, lat the user picks == the rec location in the list: true

        #this is where i am stuck, 
        if longLatGamePick == "A" or longLatGamePick == "a":
            money += 1
        elif longLatGamePick == "B" or longLatGamePick == "b":
            money += 0
        elif longLatGamePick == "C" or longLatGamePick == "c":
            money += 0
        else:
            money += 0



        runTime -= 1
        #print(runTime)

    return money

#------------Start pokemon functions-------------
#this is the function to call the pokemon game
def pokeMonGame(cash):
    money = cash
    pokiemon = []

    print("\t\t------Welcome User To the Slots-----\n")




    userPick = input("\t\t-0 is to quit-\n What Slot would you like to do user(1-3)?: ")


    while userPick != "1" and userPick != "2" and userPick != "3" and userPick != "0":
        userPick = input("\t---Silly user you have to enter '1-3' an 0 to quit: ")



    while userPick != "0":
        if userPick == "1" and money >= 5:
            prize = pokeGame1All()
            pokiemon.append(prize)
            money -= 5
        elif userPick == "2" and money >= 10:
            print("2")
            money -= 10
        elif userPick == "3" and money >= 20:
            print("3")
            money -= 20
        else:
            print("\t\t------Broke boy--------")
            
            





        userPick = input("\t\t-0 is to quit-\n What Slot would you like to do user?: ")

        while userPick != "1" and userPick != "2" and userPick != "3" and userPick != "0":
            userPick = input("\t---Silly user you have to enter '1-3' an 0 to quit: ")

    return money, pokiemon
        
#----------Sub pokemon-----------------
#sub pokemon slot games: this is the different slot functions only have the 1 slot now
def pokeGame1All():
    allPokemonran = random.randint(0, len(pokeAll))

    if allPokemonran > len(pokeNum):
        print("\n\t\t-------PokemonRan number over---------")
        allPokemonran -= 1
    clear()#clear the screen
    print("----3----")#the count down 3
    time.sleep(1)
    print("---2---") #2
    time.sleep(1)
    print("--1--")# 1
    time.sleep(1)

    #print(pokeAll[721][11])
    print(f"\t\t----You got #{pokeAll[allPokemonran][0]}: {pokeAll[allPokemonran][1]}----\nThey are a {pokeAll[allPokemonran][2]} and a {pokeAll[allPokemonran][3]} type.\n They are from gen {pokeAll[allPokemonran][10]}.\n\t----Are they a lengendary---\n\t\t{pokeAll[allPokemonran][11]}")# this is the pokiemon the user got, based on the pick they choose.
    

    wonPrize = pokeAll[allPokemonran]
    time.sleep(6)
    clear()
    return wonPrize
#Need to have the other 3 for gen and leg.

#----------------------This is where i will have my main code------------------------------------

#this is the main code to have everything

print("\t~~~~Welcome to my project!~~~~")
print("\n\t---What would you like to do user?---")

gamePick = int(menu())


while gamePick != 4:

    if gamePick == 1:
        coins = longLatGame(coins)
        print(f"Total$: {coins}")
    elif gamePick == 2:
        coins, playerPokemon = pokeMonGame(coins)
        print(f"Total$: {coins}")
    else:
        print("-------Still working----------")

    gamePick = int(menu())


input("----------------------Enter to Stop-----------------")






#The long and lat game is done, need to change prints around and clean up but main code there (if i can some how have time at end to fix the qustions than do it if not its okay wont b e much point lost)


#Need to work on the pokemon functions for the other slots

#need to work on the finding pokiemon(Just be a display of the pokiemon the user has. --------Nothing specal--------)



