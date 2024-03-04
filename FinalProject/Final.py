#David Punchak














##################-------------Imports------------############
import random
import csv
import time
from os import system, name 


###########----------------Setting Vars / lists----------------##################



################----------------Functions--------------##############
#just the clear function
def clear():

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

#function for checking userinput
def userInputYorN(userInput):
    userTester = ['y','n','Y','N']

    while userInput not in userTester:
        userInput = input("Please Enter (Y | N): ")

    return userInput





##############--------------Main Code-------------#################

print("\t\t----Welcome user to the maze-----")
time.sleep(2)

mazeGamePlay = input("\n\tDo you wish to enter?  ")

mazeGamePlay = userInputYorN(mazeGamePlay)


while mazeGamePlay.lower() == 'y':
    clear()












    #keep at the end to see if the user wants to play again or get out the loop
    mazeGamePlay = userInputYorN(mazeGamePlay)

print("\n\n\t\t----I hope you liked my project----")

input("\n\t\t------Press 'Enter' to leave-------")