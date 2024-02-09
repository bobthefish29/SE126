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

#the vars for the projects
randDeside = 0
coins = 0
live = 3


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
        pokeGen.append(int(rec[10]))
        pokeLeg.append(rec[11])
#Out of loop


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

def longLatGame(hp, money):
    #The starting for the game
    round = 10


    #printing for the user to read
    print("------This game is hard------\n")
    print(f"\tYour Total hp: {hp}")
    print(f"\tYou have: {money}")
    gamePicker = input("\nGame 1 more money, more Qustions\nGame 2 less money, less qustions\n\n(1 or 2): ")
    while gamePicker != "1" and gamePicker != "2":
        print("wrong")
        gamePicker = input("\nGame 1 more money, more Qustions\nGame 2 less money, less qustions\n\n(1 or 2): ")

    
    print("\n------Good luck------")



    #THis is the sleep function, it pauses the terminal than the clear function clears the terminal
    time.sleep(3)
    clear()
    
    
    while hp > 0 and round != 0:
        
        if gamePicker == "1":
            copyList = []
            copyList = longLat2d
            print(copyList)
            gameList = []
            rand_num = 0
            start_len = len(copyList)
            index = 0
            
            while index < start_len:
                #THis is sorting the list to make it into a random list
                print(f"\n------1Run time: {index}------------")
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
                #print(gameList)
                #print(f"Before{copyList}")

                #print(f"\n2Run time: {index}")
                #print(f"2Rand num: {rand_num}")
                copyList.pop(rand_num)
                #print(f"2Copy len:{len(copyList)}")
                #print(f"after{copyList}")
                #print(f"\n3Run time: {index}")
                #print(f"3Rand num: {rand_num}")
                index += 1

            print(gameList)


            #----------------------------Up to point of trying to get print to work. i have a lot to go :)
            print("--------------------")
            #print(ranList)

            
            randomPlace = random.randint(0, len(gameList))
            randomPlace1 = random.randint(0, len(gameList))
            randomPlace2 = random.randint(0, len(gameList))
            
            if randomPlace == -1:
                    randomPlace = 0
            elif randomPlace >= len(gameList):
                    randomPlace -= 1

            printlist = []

            printlist2 = []
            printlist3 = []
            printlist4 = []

            for i in range(0, len(gameList)):
                printlist.append(gameList[1][0])

                printlist2.append(gameList[1][1])
                printlist3.append(gameList[2][1])
                printlist4.append(gameList[1][0])
            print(printlist)



            print(f"What is the location of {printlist[randomPlace]}")


            print(f"A. {printlist2[randomPlace]}")



            #1
            #print(f"What is the location of {location[ranlonglat]}")

            #ranList.append(long[there], lat[there])

            
            
            #print(there)
            #print(f"\nA. Long {long[ranlonglat]}, Lat: {lat[ranlonglat]}  ")

            #print(f"B. {ranList[there]} ")
            #print(f"c. {ranList[there]} ")


            #print(f"B. {ranList[there]}")
            #print(f"c. {ranList[there]}")
            #print(f"D. {ranList[there]}")

            #print(f"C. Long {long[redHar2]}, Lat: {lat[redHar2]}  ")
            #print(f"D. Long {long[redHar3]}, Lat: {lat[redHar3]}  ")

            longLatGamePick = input("\nWhat is your answer: ")

            while longLatGamePick != "A" and longLatGamePick != "a" and longLatGamePick != "B" and longLatGamePick != "b" and longLatGamePick != "C" and longLatGamePick != "c" and longLatGamePick != "D" and longLatGamePick != "d":
                print("-------You Have to pick A,B,C,D silly---------")
                longLatGamePick = input("\nWhat is your answer: ")


        



            

            





    return money
    


#

#----------------------This is where i will have my main code------------------------------------

#this is the main code to have everything

print("\t~~~~Welcome to my project!~~~~")
print("\n\t---What would you like to do user?---")

gamePick = int(menu())


while gamePick != 4:

    if gamePick == 1:
        coins = longLatGame(live, coins)
        print("out of long lat")
    elif gamePick == 2:
        print(" '2'  ")
    else:
        print(" '3'  ")

    gamePick = int(menu())


input("----------------------Stop-----------------")












