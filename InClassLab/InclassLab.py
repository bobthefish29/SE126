#David punchak
#brandon emdeiros
#2/27/24
#in class lab, plain seatting chart


#-----------------------Code---------------------------------
#               0              1                     2               3                   4                    5             6
list = [["a","b","c","d"],["a","b","c","d"],["a","b","c","d"],["a","b","c","d"],["a","b","c","d"],["a","b","c","d"],["a","b","c","d"]]

#importing
from os import system, name 

#the clear function
def clear():

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


#this is the defening vars
userInput = "y"
userRow = - 1


#--------------------------------This is the setting the value of x to the location the user selected-------------------
def pickLocation(row, seat):
    space = "y"

    x = 0

    for i in range(0, len(list[0])):
        #testList = [list[0][x], list[1][x + 1], list[2][x + 1]]
        testList = list
        #x += 1

    
    #this is if seat = the value than setting it to a number
    if seat == "a":
        seatvalue = 0
    elif seat == "b":
        seatvalue = 1
    elif seat == "c":
        seatvalue = 2
    else:
        seatvalue = 3
    
    
    #this is if the location is an x than it says it but if not than it sets it to x
    if list[row][seatvalue] == "x":
        space = "n"
    else:
        testList[row][seatvalue] = "x"
    
    #returning the list and if the space is open or not
    return testList , space
    

#this is the menu to print for the user
def menu():
    print("| row  |  - - - - ")
    for i in range(0 , len(list)):
        print(f"|   {i + 1}  | {list[i][0]}   {list[i][1]}   {list[i][2]}   {list[i][3]}|")
        #print(f"| {i + 1} {str(list[i][0]):2f} {str(list[i][1]):2f} {str(list[i][2]):2f} {str(list[i][3]):2f}")

#------------Main code-------

print("----------welcome user--------------")


menu()

userInputOkay = ["y", "Y", "n", "N"]
#This to have the user 
#userInput = input("\nWish to see the menu: ")

while userInput == "y" or userInput == "Y":
    
    if userInput == "y":
        
        #this is to trap the user row and make sure its a number


        while userRow < 1 or userRow > 7:
            try:
                userRow = int(input("\nPlease enter a Row (1-7): "))
            except:
                print("Invalid integer, enter a number!")
            



        #this is the same for the row but for the seat input
        userseat = input("What seat: ")
        userseatOkay = ["a", "b", "c", "d", "A", "B", "C", "D"]

        while userseat not in userseatOkay:
            userseat = input("What seat (A,B,C,D): ")
            

        #This is to be sure the user gets there row

        if userRow == 0:
            userRow = 0
        else:
            userRow -= 1


        

        input(f"Does row {userRow + 1} seat {userseat.lower()} look good?")
        #input("\n\tDoes the seat feel nice 'Enter' to be sure?")

        list, space = pickLocation(userRow, userseat)

        clear()
        menu()
        if space == "y":
            print("\n\t-----That seat is open-----")
        else:
            print("\n\t----That seat is taken-------")


    #this is to trap the user input for the loop

    userseat = ""
    userRow = - 1

    #userInputOkay = ["y", "Y", "n", "N"]

    userInput = input("\nWish to keep going: ")

    while userInput not in userInputOkay:
        userInput = input("\nWish to keep going (Y \ N ): ")


#having the end of the project
input('----------Thank you user "enter to quit"--------')






    







